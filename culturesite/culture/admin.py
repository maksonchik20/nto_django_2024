from django.contrib import admin
from .models import Artifact, ForeignOrganization, ShowcaseType, Showcase, ArtifactReturnAct, ShowcaseOrder
from import_export.admin import ImportExportModelAdmin
from .resources import ArtifactResource, ForeignOrganizationResource, ShowcaseTypeResource, ShowcaseResource, ArtifactReturnActResource
from django import forms


class ArtifactForm(forms.ModelForm):
    def clean(self):
        owner_study = self.cleaned_data['owner_study']
        owner_foreign_organization = self.cleaned_data['owner_foreign_organization']
        if owner_study is None and owner_foreign_organization is None:
            raise forms.ValidationError({
                'owner_study': "Владелец не выбран"
            })
        
        if owner_study is not None and owner_foreign_organization is not None:
            raise forms.ValidationError({
                'owner_foreign_organization': "Выберите одного владельца"
            })


@admin.register(Artifact)
class ArtifactAdmin(ImportExportModelAdmin):
    form = ArtifactForm
    list_display = ["name", "owner", "id"]
    resource_class = ArtifactResource


@admin.register(ForeignOrganization)
class ForeignOrganizationAdmin(ImportExportModelAdmin):
    list_display = ["name", "id"]
    resource_class = ForeignOrganizationResource


@admin.register(ShowcaseType)
class ShowcaseTypeAdmin(ImportExportModelAdmin):
    list_display = ["name", "id"]
    resource_class = ShowcaseTypeResource


@admin.register(Showcase)
class ShowcaseAdmin(ImportExportModelAdmin):
    list_display = ["name", "type", "id"]
    resource_class = ShowcaseResource

    def clean(self):
        showcase = self.cleaned_data['showcase'] 
        atrifacts = self.cleaned_data['atrifacts'] 
        print(showcase, atrifacts)
        return self.cleaned_data



@admin.register(ArtifactReturnAct)
class ArtifactReturnActAdmin(ImportExportModelAdmin):
    list_display = ["showcase_order", "datetime", "id"]
    resource_class = ArtifactReturnActResource
    
admin.site.register(ShowcaseOrder)
