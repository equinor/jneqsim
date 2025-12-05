import tempfile
from pathlib import Path

import pytest
import yaml


@pytest.fixture(scope="session")
def sample_neqsim_config():
    """Sample NeqSim configuration for testing."""
    return {
        "neqsim": {
            "version": "3.1.2",
            "fallback_version": "3.1.1",
            "sources": {
                "github": {
                    "enabled": True,
                    "repository": "equinor/neqsim",
                    "base_url": "https://github.com/equinor/neqsim/releases/download",
                    "assets": {
                        "java8": "neqsim-{version}-Java8.jar",
                        "java11": "neqsim-{version}.jar",
                        "java21": "neqsim-{version}-Java21.jar",
                    },
                },
            },
        },
        "logging": {"level": "DEBUG", "show_progress": True},
    }


@pytest.fixture
def temp_config_dir():
    """Create a temporary directory for test configuration files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def sample_config_file(sample_neqsim_config, temp_config_dir):
    """Create a temporary config file with sample configuration."""
    config_file = temp_config_dir / "test_dependencies.yaml"
    with open(config_file, "w") as f:
        yaml.dump(sample_neqsim_config, f)
    return config_file


@pytest.fixture
def temp_cache_dir():
    """Create a temporary cache directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir) / "cache"


def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line("markers", "slow: mark test as slow (may download files)")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "unit: mark test as unit test")
