from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from ..models import Item, UserLike, UserSave, UserView

class TrackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        item_id = request.data.get("item_id")
        view_duration = int(request.data.get("view_duration", 0))
        item = Item.objects.filter(id=item_id).first()
        if not item:
            return Response({"error": "Item not found"}, status=404)

        UserView.objects.create(user=request.user, item=item, view_duration=view_duration)
        Item.objects.filter(id=item_id).update(view_count=item.view_count + 1)
        return Response({"success": True})

class ToggleLike(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, item_id):
        item = Item.objects.filter(id=item_id).first()
        if not item:
            return Response({"error": "Item not found"}, status=404)

        existing = UserLike.objects.filter(user=request.user, item=item).first()
        if existing:
            existing.delete()
            Item.objects.filter(id=item_id).update(like_count=max(item.like_count - 1, 0))
            return Response({"success": True, "is_liked": False})

        UserLike.objects.create(user=request.user, item=item)
        Item.objects.filter(id=item_id).update(like_count=item.like_count + 1)
        return Response({"success": True, "is_liked": True})

class ToggleSave(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, item_id):
        item = Item.objects.filter(id=item_id).first()
        if not item:
            return Response({"error": "Item not found"}, status=404)

        existing = UserSave.objects.filter(user=request.user, item=item).first()
        if existing:
            existing.delete()
            Item.objects.filter(id=item_id).update(save_count=max(item.save_count - 1, 0))
            return Response({"success": True, "is_saved": False})

        UserSave.objects.create(user=request.user, item=item)
        Item.objects.filter(id=item_id).update(save_count=item.save_count + 1)
        return Response({"success": True, "is_saved": True})
