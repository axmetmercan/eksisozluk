
from rest_framework import serializers
from .models import *

class EntrySerializer(serializers.ModelSerializer):
   user = serializers.StringRelatedField(read_only = True)
   #title = serializers.StringRelatedField(read_only = True)
   like = serializers.StringRelatedField(read_only = True)
   class Meta:
      model = Explanation
      exclude = ['title', ]
      #fields = "__all__"

class CreateEntrySerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField(read_only = True)
   #title = serializers.StringRelatedField(read_only = True)
   class Meta:
      model = Explanation
      exclude = ['title','user', 'like', 'status']
      #fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
   class Meta:
      model = Tag
      exclude = ['id',]


class TitleSerialier(serializers.ModelSerializer):
   # tags = serializers.StringRelatedField(many = True)
   tags = TagSerializer(many = True)
   created_by = serializers.StringRelatedField(read_only = True)
   class Meta:
      model = Title
      #   exclude = ['id',] 
      fields = "__all__"

   def create(self, validated_data):
      tags = validated_data.pop("tags")
      title = validated_data.pop("name")
      total_click = validated_data.pop("total_click")


      nTitle = Title(name = title , total_click = total_click)         
      nTitle.save()
      print(tags)
   
      for ordered_dict in tags:
         for key, value in ordered_dict.items():         
            current_tag = Tag.objects.get(name = value)
            nTitle.tags.add(current_tag)
      return nTitle
      


class TitleDetailSerializer(serializers.ModelSerializer):
  
   entries = serializers.SerializerMethodField()
   tags = serializers.StringRelatedField(read_only = True, many = True)
   created_by = serializers.StringRelatedField(read_only = True)

   # entries = EntrySerializer(many = True, read_only = True)
   
   class Meta:
      model = Title
      fields = "__all__"



   def get_entries(self, obj):
      entries  = Explanation.objects.filter(title=obj.id)[:1]
      serializer = EntrySerializer(entries, many=True, read_only=True)
      return serializer.data

   def get_tags(self, obj):
      tags = Tag.objects.filter(title = obj.id)
      serializer = TagSerializer(tags, many=True, read_only=True)
      return serializer.data      
            

class TitleDetailSerializerMany(serializers.ModelSerializer):
  
   entries = serializers.SerializerMethodField()
   tags = serializers.StringRelatedField(read_only = True, many = True)
   created_by = serializers.StringRelatedField(read_only = True)

   # entries = EntrySerializer(many = True, read_only = True)
   
   class Meta:
      model = Title
      fields = "__all__"



   def get_entries(self, obj):
      entries  = Explanation.objects.filter(title=obj.id, status = True).order_by('created_date')
      serializer = EntrySerializer(entries, many=True, read_only=True)
      return serializer.data

   def get_tags(self, obj):
      tags = Tag.objects.filter(title = obj.id)
      serializer = TagSerializer(tags, many=True, read_only=True)
      return serializer.data      

class BlogSerializer(serializers.ModelSerializer):
   like = serializers.StringRelatedField(read_only = True)
   user = serializers.StringRelatedField(read_only = True)
   created_date = serializers.StringRelatedField(read_only = True)
   image_url = serializers.ImageField(required=False)

   class Meta:
      model = Blog
      fields = ["title", "content",'like', "user", "created_date", "image_url"]

