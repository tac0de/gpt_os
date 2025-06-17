import importlib
import gptos.plugins as plugins
import sys
import os

PLUGIN_REGISTRY = {}  # This must NEVER be reassigned after this line
PLUGIN_CACHE = {}  # 캐시 추가

def load_plugins():
    # ✅ Only clear and update, DO NOT reassign
    PLUGIN_REGISTRY.clear()

    plugin_dir = os.path.dirname(plugins.__file__)
    loaded = []

    for filename in os.listdir(plugin_dir):
        if filename.endswith("_plugin.py"):
            module_name = filename[:-3]
            module_path = f"{plugins.__name__}.{module_name}"

            # 플러그인 캐시 확인
            if module_path in PLUGIN_CACHE:
                # 캐시된 플러그인 사용
                PLUGIN_REGISTRY.update(PLUGIN_CACHE[module_path].PLUGIN_REGISTRY)
                loaded.append(module_name)
                continue

            try:
                if module_path in sys.modules:
                    # 이미 로드된 플러그인 재로딩
                    importlib.reload(sys.modules[module_path])
                else:
                    # 새로 로드
                    importlib.import_module(module_path)
                
                mod = sys.modules[module_path]
                if hasattr(mod, "PLUGIN_REGISTRY"):
                    PLUGIN_REGISTRY.update(mod.PLUGIN_REGISTRY)
                    loaded.append(module_name)

                    # 플러그인 캐시 저장
                    PLUGIN_CACHE[module_path] = mod
                else:
                    print(f"[SKIPPED] {module_name} has no PLUGIN_REGISTRY")
            except Exception as e:
                print(f"[ERROR] Failed to load {module_name}: {e}")

    print(f"[INFO] Loaded {len(loaded)} plugins")
