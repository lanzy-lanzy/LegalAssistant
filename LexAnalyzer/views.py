from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import LegalDocument
from .utils import analyze_document
from django.core.files.storage import FileSystemStorage
import os
import json

def home(request):
    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        
        # Save to database
        doc = LegalDocument.objects.create(
            title=uploaded_file.name,
            file=filename
        )
        
        # Trigger analysis
        analysis = analyze_document(file_path)
        doc.summary = analysis.get('summary', '')
        # Simple mapping for risk level
        risks = analysis.get('risks', [])
        if any(r['severity'] == 'rose' for r in risks):
            doc.risk_level = 'High'
        elif any(r['severity'] == 'amber' for r in risks):
            doc.risk_level = 'Medium'
        else:
            doc.risk_level = 'Low'
        doc.save()
        
        return redirect('analyze_doc', doc_id=doc.id)
        
    documents = LegalDocument.objects.all().order_by('-uploaded_at')[:5]
    return render(request, 'home.html', {'recent_documents': documents})

def analyze(request):
    # This might be used for general upload too
    return render(request, 'analyze.html')

def analyze_doc(request, doc_id):
    doc = LegalDocument.objects.get(id=doc_id)
    file_path = doc.file.path
    analysis = analyze_document(file_path)
    return render(request, 'analyze.html', {
        'doc': doc,
        'analysis': analysis,
        'analysis_json': json.dumps(analysis)
    })


def clauses(request):
    return render(request, 'clauses.html')


