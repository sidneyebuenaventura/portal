from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core_cms", "0024_alter_curriculumsubject_curriculum_period"),
        ("core_students", "0011_auto_20220623_0145"),
    ]

    operations = [
        migrations.RenameField(
            model_name="enrollmentsubjectschedule",
            old_name="subject_class",
            new_name="klass",
        ),
        migrations.RenameModel(
            old_name="EnrollmentSubjectSchedule", new_name="EnrolledClass"
        ),
        migrations.AlterField(
            model_name="enrolledclassgrade",
            name="enrolled_class",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grade",
                to="core_students.enrolledclass",
            ),
        ),
    ]
