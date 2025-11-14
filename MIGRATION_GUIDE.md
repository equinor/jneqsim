# Migration to Runtime Dependency Management 🎉

## Overview

We have successfully migrated jNeqSim from bundled JAR files to **runtime dependency management**! This brings significant improvements:

### ✅ Benefits

- **📦 Smaller package size**: No more 50MB+ JAR files bundled in wheels
- **⚡ Faster installs**: Package downloads and installs much faster  
- **🔄 Better caching**: Dependencies cached locally, shared between projects
- **🎯 Version flexibility**: Easy to specify NeqSim versions
- **🏗️ Simpler CI/CD**: No JAR downloading during builds
- **🔮 Future-proof**: Ready for Maven Central when NeqSim publishes there

## How It Works

### Before (Old System)
1. CI/CD downloads JAR files from GitHub releases
2. JAR files bundled into Python package
3. Large package distributed to users
4. JARs loaded from package directory

### After (New System) 
1. Dependencies resolved at **runtime** when first imported
2. JARs downloaded to user cache (`~/.cache/jneqsim/`)
3. Subsequent uses load from cache (very fast)
4. Support for multiple Java versions and NeqSim versions

## Configuration

Dependencies are configured in `jneqsim/dependencies.yaml`:

```yaml
neqsim:
  version: "latest"  # or specific version like "3.1.0"
  
  sources:
    # Maven Central (checked first when available)
    maven:
      enabled: true
      coordinates:
        - groupId: "no.ntnu.neqsim"
          artifactId: "neqsim-core"
    
    # GitHub Releases (current primary source)
    github:
      enabled: true
      repository: "equinor/neqsim"
      # Different JARs for different Java versions
      assets:
        java8: "neqsim-{version}-Java8.jar"
        java11: "neqsim-{version}.jar"
        java21: "neqsim-{version}-Java21.jar"

cache:
  directory: "~/.cache/jneqsim"
  verify_integrity: true
  max_size_mb: 500
  ttl_days: 30
```

## Usage (No Changes Required!)

The API remains exactly the same:

```python
from jneqsim import neqsim

# Works exactly as before!
system = neqsim.thermo.system.SystemSrkEos()
system.addComponent("methane", 100.0)
```

### Advanced Usage (New Capabilities)

```python
from jneqsim.dependency_manager import NeqSimDependencyManager

# Create manager
manager = NeqSimDependencyManager()

# Use specific version
jar_path = manager.resolve_dependency(version="3.0.0", java_version=11)

# Clear cache
manager.clear_cache()

# List cached versions
cached = manager.list_cached_versions()
print(cached)
```

## Implementation Details

### Core Components

1. **`NeqSimDependencyManager`** (`jneqsim/dependency_manager.py`)
   - Handles dependency resolution
   - Manages local cache
   - Supports Maven Central + GitHub fallback
   - Integrity verification with SHA-256

2. **Enhanced JVM Service** (`jneqsim/jvm_service.py`)
   - Uses dependency manager for JAR resolution
   - Maintains same API for backward compatibility
   - Graceful handling when JPype not available

3. **Configuration** (`jneqsim/dependencies.yaml`)
   - YAML-based configuration
   - Support for multiple dependency sources
   - Caching and logging configuration

### Dependency Resolution Flow

1. **Check cache** - Look for already downloaded JAR
2. **Try Maven Central** - If enabled and available
3. **Fall back to GitHub** - Download from releases
4. **Verify integrity** - SHA-256 checksum validation
5. **Update cache** - Store for future use

### Cache Management

- **Location**: `~/.cache/jneqsim/`
- **TTL**: Configurable expiration (default 30 days)
- **Size limits**: Automatic cleanup of old files
- **Integrity**: SHA-256 verification on cache hits
- **Manifest**: JSON file tracking cached dependencies

## Migration Impact

### For Users
- ✅ **No code changes required** - API remains the same
- ✅ **Faster installation** - Much smaller package
- ✅ **First-run setup** - Automatic dependency download
- ✅ **Better performance** - Cached dependencies load instantly

### For Developers  
- ✅ **Simpler workflows** - No JAR downloading in CI/CD
- ✅ **Easier testing** - Test with different NeqSim versions
- ✅ **Better debugging** - Clear dependency resolution logs
- ✅ **Future flexibility** - Easy to add new dependency sources

### For CI/CD
- ✅ **Faster builds** - No JAR downloads during build
- ✅ **Smaller artifacts** - Package ~95% smaller
- ✅ **Less complexity** - Fewer build steps
- ✅ **Better reliability** - No dependency on external downloads during build

## File Changes

### Modified Files
- `jneqsim/jvm_service.py` - Enhanced with dependency manager
- `pyproject.toml` - Added PyYAML, removed JAR includes
- `.github/workflows/tests.yaml` - Removed JAR download steps
- `.github/workflows/publish.yaml` - Removed JAR download steps

### New Files
- `jneqsim/dependency_manager.py` - Core dependency management
- `jneqsim/dependencies.yaml` - Configuration file

### Removed Dependencies
- No more bundled JAR files in package
- Simplified CI/CD workflows

## Future Enhancements

When NeqSim publishes to Maven Central:
1. Update `dependencies.yaml` with correct coordinates
2. Enable Maven source in configuration  
3. Automatic fallback still available

## Testing

Run the test script to verify everything works:

```bash
# Test basic dependency resolution
python test_dependency_only.py

# Test with full functionality (requires JPype1)
python test_dependency_management.py
```

## Troubleshooting

### Clear Cache
```python
from jneqsim.dependency_manager import NeqSimDependencyManager
manager = NeqSimDependencyManager()
manager.clear_cache()
```

### Check Cache Status
```python
manager = NeqSimDependencyManager()
cached = manager.list_cached_versions()
for item in cached:
    print(f"{item['version']} - {item['size_mb']} MB")
```

### Manual Configuration
Edit `jneqsim/dependencies.yaml` to customize:
- NeqSim version
- Cache location
- Enable/disable Maven checking
- Logging levels

---

🎉 **Migration Complete!** Your Python package is now much more efficient with runtime dependency management.