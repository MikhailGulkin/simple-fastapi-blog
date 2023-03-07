import pytest

from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
async def test_get_all_posts(
        client: AsyncClient,
        create_user_in_database,
        user_data,
        create_post_in_database,
        post_data
) -> None:
    await create_user_in_database(**user_data)
    await create_post_in_database(**post_data)

    response = await client.get('/post/get-all-post')

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list) is True
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_get_post(
        client: AsyncClient,
        create_user_in_database,
        user_data,
        create_post_in_database,
        post_data
) -> None:
    await create_user_in_database(**user_data)
    await create_post_in_database(**post_data)

    response = await client.get(f'/post/get-post/{post_data["post_id"]}')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['summary'] == post_data['summary']


@pytest.mark.asyncio
async def test_create_post(
        client: AsyncClient,
        user_data,
        create_user_in_database
) -> None:
    await create_user_in_database(**user_data)

    data_json = {
        "author_id": user_data['user_id'],
        "title": "string",
        "summary": "string",
        "body": "string"
    }
    response = await client.post(
        f'/post/create-post',
        json=data_json
    )

    json = response.json()

    assert response.status_code == status.HTTP_201_CREATED

    assert json['title'] == data_json['title']
    assert json['body'] == data_json['body']


@pytest.mark.asyncio
async def test_update_post(
        client: AsyncClient,
        create_user_in_database,
        user_data,
        create_post_in_database,
        post_data
) -> None:
    data_json = {
        "title": "string123",
        "summary": "string123",
        "body": "string123"
    }

    await create_user_in_database(**user_data)
    await create_post_in_database(**post_data)

    response = await client.patch(
        f'/post/update-post/{post_data["post_id"]}',
        json=data_json
    )
    json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert json['title'] == data_json['title']
    assert json['summary'] == data_json['summary']


@pytest.mark.asyncio
async def test_delete_post(
        client: AsyncClient,
        create_user_in_database,
        user_data,
        create_post_in_database,
        post_data
) -> None:
    await create_user_in_database(**user_data)
    await create_post_in_database(**post_data)

    response = await client.delete(f'/post/delete-post/{post_data["post_id"]}')

    assert response.status_code == status.HTTP_204_NO_CONTENT
