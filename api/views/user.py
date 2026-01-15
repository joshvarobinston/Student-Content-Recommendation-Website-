from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import UserInterest, UserSettings, UserSave, UserLike
from ..serializers import UserSerializer, SettingsSerializer, ItemSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

class UpdateInterestsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        interests = request.data.get("interests", [])
        if not isinstance(interests, list):
            return Response({"error": "interests must be a list"}, status=400)

        UserInterest.objects.filter(user=request.user).delete()
        for d in interests:
            UserInterest.objects.create(user=request.user, interest_domain=str(d))

        return Response({"success": True, "interests": interests})

class SettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        s, _ = UserSettings.objects.get_or_create(user=request.user)
        return Response(SettingsSerializer(s).data)

    def put(self, request):
        s, _ = UserSettings.objects.get_or_create(user=request.user)
        ser = SettingsSerializer(s, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"success": True, "settings": ser.data})

class SavedItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = [x.item for x in UserSave.objects.filter(user=request.user).select_related("item")]
        return Response(ItemSerializer(items, many=True).data)

class FavoriteItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = [x.item for x in UserLike.objects.filter(user=request.user).select_related("item")]
        return Response(ItemSerializer(items, many=True).data)
