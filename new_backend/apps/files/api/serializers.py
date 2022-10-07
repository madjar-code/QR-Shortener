from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('input_excel_file', )
