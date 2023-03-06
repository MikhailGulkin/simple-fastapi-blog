import pytest

from httpx import AsyncClient
from fastapi import status
from sqlalchemy import select

from tests.factory.user import UserFactory


@pytest.mark.asyncio
async def test_get_all_users(
        client: AsyncClient,
) -> None:
    UserFactory.create_batch(10)
    response = await client.get('/user/get-all-user')

    assert response.status_code == status.HTTP_200_OK
    print(response.json())
