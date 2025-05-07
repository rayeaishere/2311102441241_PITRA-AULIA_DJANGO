from django.shortcuts import render
from blog.views import fetch_articles
# Create your views here.
def homepage(request):
    articles = [
        {"title": "Fashion Spring 2025", "summary": "Highlights from Spring collection.", "url": "#", "urlToImage": "https://fashionmagazine.mblycdn.com/fm/resized/2024/10/w1200/launchmetrics.comspotlight-for-the-imagerydesign-by-Lindsay.jpg"},
        {"title": "Streetwear Trend", "summary": "What's hot in streetwear.", "url": "#", "urlToImage": "https://data2.nssmag.com/images/galleries/20114/streetwear-1024x683.jpg"},
        {"title": "Sustainable Brands", "summary": "Eco-friendly fashion brand to follow.", "url": "#", "urlToImage": "https://media1.popsugar-assets.com/files/thumbor/awGyS-LAzgaZN28zNT2l2_oG2uw/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2022/09/06/894/n/1922564/0d06ddc25d96161c_GettyImages-1175059628/i/London-Fashion-Week.jpg"},
    ]
    
    return render(request, 'home/index.html', {'articles': articles})