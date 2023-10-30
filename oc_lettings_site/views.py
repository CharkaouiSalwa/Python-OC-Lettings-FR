from django.shortcuts import render

# Create your views here.
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.


def index(request):
    return render(request, 'index.html')


# Vue personnalisée pour l'erreur 404 (Page not found)
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


# Vue personnalisée pour l'erreur 500 (Server error)
def custom_server_error(request):
    return render(request, '500.html', status=500)
