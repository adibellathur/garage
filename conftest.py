"""Place Pytest fixtures to be used across all tests here."""
import pytest
import ray


@pytest.fixture(scope='session', autouse=True)
def setup_ray_local():
    """Initializes Ray in localmode before session starts."""
    if not ray.is_initialized():
        ray.init(memory=52428800,
                 object_store_memory=78643200,
                 ignore_reinit_error=True,
                 log_to_driver=False)


@pytest.fixture(scope='session', autouse=True)
def cleanup_ray(request):
    """Cleanup a testing directory once we are finished.

    Args:
        request(request_context): Used for introspect the requesting test
            function, class or module context.

    """

    def shutdown_ray():
        if ray.is_initialized():
            ray.shutdown()

    request.addfinalizer(shutdown_ray)
