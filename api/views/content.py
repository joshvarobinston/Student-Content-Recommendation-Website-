from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from ..models import Item, UserSearch
from ..serializers import ItemSerializer

class SearchView(APIView):
    def get(self, request):
        q = request.GET.get("q", "").strip()
        ctype = request.GET.get("type", "").strip()
        sort = request.GET.get("sort", "newest").strip()
        limit = min(int(request.GET.get("limit", 20)), 50)

        if not q:
            return Response({"error": "q is required"}, status=400)

        qs = Item.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))

        if ctype:
            qs = qs.filter(source_type=ctype)

        if sort == "popular":
            qs = qs.order_by("-view_count", "-like_count", "-save_count")
        else:
            qs = qs.order_by("-published_date", "-created_at")

        results = ItemSerializer(qs[:limit], many=True).data

        if request.user.is_authenticated:
            UserSearch.objects.create(user=request.user, query=q, results_count=len(results))

        return Response({"query": q, "results_count": len(results), "results": results})
