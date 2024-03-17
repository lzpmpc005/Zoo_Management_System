# Generated by Django 4.2.7 on 2024-03-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("digitalzoo", "0014_remove_tourschedule_guided_tours_guidedtour_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tourschedule",
            old_name="habitats",
            new_name="habitat",
        ),
        migrations.RenameField(
            model_name="tourschedule",
            old_name="members",
            new_name="member",
        ),
        migrations.RemoveField(
            model_name="tourschedule",
            name="guided_tours",
        ),
        migrations.RemoveField(
            model_name="tourschedule",
            name="habitat_availability",
        ),
        migrations.RemoveField(
            model_name="tourschedule",
            name="visitor_feedback",
        ),
        migrations.AddField(
            model_name="tourschedule",
            name="animal",
            field=models.ManyToManyField(blank=True, to="digitalzoo.animal"),
        ),
        migrations.DeleteModel(
            name="GuidedTour",
        ),
    ]
