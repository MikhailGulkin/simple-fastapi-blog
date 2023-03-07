import pytest

from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
async def test_get_all_users(
        client: AsyncClient,
        create_user_in_database,
        user_data
) -> None:
    await create_user_in_database(**user_data)
    response = await client.get('/user/get-all-user')

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list) is True
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_get_user(
        client: AsyncClient,
        create_user_in_database,
        user_data
) -> None:
    await create_user_in_database(**user_data)
    response = await client.get(f'/user/get-user/{user_data["user_id"]}')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == user_data['username']


@pytest.mark.asyncio
async def test_create_user(
        client: AsyncClient,
) -> None:
    data_json = {
        'username': '123',
        'email': '123@mail.com',
        'password': '123'
    }
    response = await client.post(
        f'/user/create-user',
        json=data_json
    )

    json = response.json()

    assert response.status_code == status.HTTP_201_CREATED

    assert json['username'] == data_json['username']
    assert json['email'] == data_json['email']


@pytest.mark.asyncio
async def test_update_user(
        client: AsyncClient,
        create_user_in_database,
        user_data
) -> None:
    update_data = {
        'username': "upd_username",
        'email': "upd_username",
        'password': 'upd_password'
    }

    await create_user_in_database(**user_data)

    response = await client.patch(
        f'/user/update-user/{user_data["user_id"]}',
        json=update_data
    )
    json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert json['username'] == update_data['username']
    assert json['email'] == update_data['email']


@pytest.mark.asyncio
async def test_delete_user(
        client: AsyncClient,
        create_user_in_database,
        user_data
) -> None:
    await create_user_in_database(**user_data)
    response = await client.delete(f'/user/delete-user/{user_data["user_id"]}')

    assert response.status_code == status.HTTP_204_NO_CONTENT
