# Generated manually to handle django-taggit transition

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_tag_post_tags"),
        ("taggit", "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx"),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]