from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name','roll','city']