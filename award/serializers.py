from rest_framework import serializers

from award.models import Award, AwardCategory


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('award_category', 'member', 'attained')

class AwardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCategory
        fields = ('title', 'description', 'members')
