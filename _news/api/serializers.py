from rest_framework import serializers
from _news.models import Article, Journalist


class JournalistSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    biography = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        return Journalist.objects.create(**validated_data)

        '''
        validated_data arkaplanda bir dictionary objesi
        dolayısıyla iki tane yıldız işareti koymalıyız ki
        bu  objeyi aç anahtar değer alanlarını eşleştir
        ve kaydet dememiz lazım
        '''

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.biography = validated_data.get(
            'biography', instance.biography)

        instance.save()
        return instance
        '''
        ben update sırasında karşı tarafa bir instance göneriyorum
        bu  objede update edilecek alan var mı yok ona bakmam lazım
        '''


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    journalist_id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    publish_date = serializers.DateField()
    is_active = serializers.BooleanField()
    creation_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

        '''
        validated_data arkaplanda bir dictionary objesi
        dolayısıyla iki tane yıldız işareti koymalıyız ki
        bu  objeyi aç anahtar değer alanlarını eşleştir
        ve kaydet dememiz lazım
        '''

    def update(self, instance, validated_data):

        instance.journalist = validated_data.get(
            'journalist', instance.journalist)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.publish_date = validated_data.get(
            'publish_date', instance.publish_date)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)

        '''
            yaratılma ve güncellenme tarihini almadık çünkü bunlarla ilgili işlem yapılmıyor
        '''
        instance.save()
        return instance
    '''
        ben update sırasında karşı tarafa bir instance göneriyorum
        bu  objede update edilecek alan var mı yok ona bakmam lazım
    '''

    def validate(self, data):
        if data['title'] == data['text']:
            raise serializers.ValidationError(
                "(title) ve (text) alanları aynı olamaz")
        return data
    
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                f"(title) alanı en az 20 karakter içermelidir, siz {len(value)} karakter kullandınız"
            )
        return value
