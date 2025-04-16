import requests
from django.http import JsonResponse

def get_fashion_articles(request):
    # Kirim permintaan ke API berita
    response = requests.get(
        'https://newsapi.org/v2/everything',
        params={
            'q': 'fashion',              # cari artikel tentang fashion
            'sortBy': 'publishedAt',     # urutkan berdasarkan yang terbaru
            'language': 'en',            # pakai bahasa inggris
            'apiKey': 'API_KEY_KAMU'     
        }
    )

    return JsonResponse(response.json())
