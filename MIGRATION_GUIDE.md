# Migration to Runtime Dependency Management 🎉

## Overview

We have successfully migrated jNeqSim from bundled JAR files to **runtime dependency management**! This brings significant improvements:

### ✅ Benefits

- **📦 Smaller package size**: No more 50MB+ JAR files bundled in wheels
- **⚡ Faster installs**: Package downloads and installs much faster  
- **🎯 Version flexibility**: Easy to specify NeqSim versions
- **🏗️ Simpler CI/CD**: No JAR downloading during builds
- **🔮 Streamlined architecture**: Direct GitHub downloads without complex caching

## How It Works

### Before (Old System)
1. CI/CD downloads JAR files from GitHub releases
2. JAR files bundled into Python package
3. Large package distributed to users
4. JARs loaded from package directory

### After (New System) 
1. Dependencies resolved at **runtime** when first imported
2. JARs downloaded directly from GitHub releases to temporary locations
3. Support for multiple Java versions and NeqSim versions
4. Simple, straightforward download process

## Configuration

Dependencies are configured in `jneqsim/dependencies.yaml`:

```yaml
neqsim:
  version: "latest"  # or specific version like "3.1.0"
  
  # GitHub Releases source
  sources:
    github:
      enabled: true
      repository: "equinor/neqsim"
      # Different JARs for different Java versions
      assets:
        java8: "neqsim-{version}-Java8.jar"
        java11: "neqsim-{version}.jar"
        java21: "neqsim-{version}-Java21.jar"

logging:
  level: "INFO"
  show_progress: true
```

## Usage (No Changes Required!)

The API remains exactly the same:

```python
from jneqsim import neqsim

# Works exactly as before!
system = neqsim.thermo.system.SystemSrkEos()
system.addComponent("methane", 100.0)
```

### Advanced Usage

```python
from jneqsim.dependency_manager import NeqSimDependencyManager

# Create manager
manager = NeqSimDependencyManager()

# Use specific version
jar_path = manager.resolve_dependency(version="3.0.0", java_version=11)
print(f"JAR downloaded to: {jar_path}")
```

## Implementation Details

### Core Components

1. **`NeqSimDependencyManager`** (`jneqsim/dependency_manager.py`)
   - Handles dependency resolution
   - Downloads JARs from GitHub releases
   - Supports multiple Java versions
   - URL validation for security

2. **Enhanced JVM Service** (`jneqsim/jvm_service.py`)
   - Uses dependency manager for JAR resolution
   - Maintains same API for backward compatibility
   - Graceful handling when JPype not available

3. **Configuration** (`jneqsim/dependencies.yaml`)
   - YAML-based configuration
   - GitHub releases configuration
   - Logging configuration

### Dependency Resolution Flow

1. **Check version** - Determine NeqSim version to use
2. **Resolve JAR type** - Select appropriate JAR for Java version
3. **Download from GitHub** - Download JAR from GitHub releases
4. **Validate security** - URL validation before download
5. **Return path** - Provide path to downloaded JAR

## Migration Impact

### For Users
- ✅ **No code changes required** - API remains the same
- ✅ **Faster installation** - Much smaller package
- ✅ **Automatic setup** - Dependency download on first use
- ✅ **Simple architecture** - Direct downloads when needed

### For Developers  
- ✅ **Simpler workflows** - No JAR downloading in CI/CD
- ✅ **Easier testing** - Test with different NeqSim versions
- ✅ **Better debugging** - Clear dependency resolution logs
- ✅ **Streamlined code** - Simplified dependency manager

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

Potential future improvements:
1. Add local caching for frequently used JARs
2. Support for Maven Central when NeqSim is published there
3. Automatic cleanup of temporary files
4. Version pinning and dependency locking

## Testing

Run the test script to verify everything works:

```bash
# Test basic dependency resolution
python test_dependency_only.py

# Test with full functionality (requires JPype1)
python test_dependency_management.py
```

## Troubleshooting

### Manual Configuration
Edit `jneqsim/dependencies.yaml` to customize:
- NeqSim version
- GitHub repository settings
- Logging levels

### Check Download Status
```python
from jneqsim.dependency_manager import NeqSimDependencyManager
manager = NeqSimDependencyManager()

# Test download
jar_path = manager.resolve_dependency()
print(f"Downloaded JAR to: {jar_path}")
```

---

🎉 **Migration Complete!** Your Python package is now much more efficient with simplified runtime dependency management.