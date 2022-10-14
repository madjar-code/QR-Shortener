from rest_framework.serializers import \
    ModelSerializer,\
    SerializerMethodField
from files.models import Session
from shortener.models import Link
from shortener.api.serializers import LinkSerializer


class SimpleSessionSerializer(ModelSerializer):
    one_url = SerializerMethodField()

    def get_one_url(self, obj):
        own_links = Link.objects.filter(session=obj)
        if (len(own_links) > 1) or\
           (len(own_links) == 0):
            return None
        return own_links[0].long_url

    class Meta():
        model = Session
        fields = '__all__'

class SessionSerializer(ModelSerializer):
    own_links = LinkSerializer(many=True)
    class Meta():
        model = Session
        fields = '__all__'
