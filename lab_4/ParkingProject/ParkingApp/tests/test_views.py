import pytest 
from django.urls import reverse
from constans import USER_VIEW, OTHER_VIEW
from ParkingApp.models import Auto


@pytest.mark.parametrize('view', OTHER_VIEW)
@pytest.mark.django_db
def test_general_access(user, client, view):
    response = client.get(reverse(view))
    assert response.status_code == 200


@pytest.mark.parametrize('view', USER_VIEW)
@pytest.mark.django_db
def test_user_access(user, client, view):
    client.force_login(user)
    response = client.get(reverse(view))
    assert response.status_code == 200


@pytest.mark.parametrize('view', USER_VIEW)
@pytest.mark.django_db
def test_nonuser_access(user, client, view):
    response = client.get(reverse(view))
    assert response.status_code == 302


@pytest.mark.django_db
def test_auto_crud(user, client):
    client.force_login(user)

    form_data = {'model' : 'testCRUD', 'brand' : 'testbrand'}
    response = client.post(reverse('create_auto'), data=form_data)
    assert response.status_code == 200

    pk = Auto.objects.get(model='testCRUD', brand='testbrand').id
    form_data = {'model' : 'testCRUD', 'brand' : 'editbrand'}
    response = client.post(reverse('edit_auto', kwargs={'id' : pk, }), data=form_data)
    assert response.status_code == 302

    pk = Auto.objects.get(model='testCRUD', brand='editbrand').id
    response = client.post(reverse('delete_auto', kwargs={'id' : pk, }))
    assert response.status_code == 302