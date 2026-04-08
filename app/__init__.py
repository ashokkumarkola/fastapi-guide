# package marker
# Every importable directory MUST contain __init__.py

# -----------------------------------------------

# Best Architecture (Clean & Flexible)

# app/
# ├── main.py          # create_app()
# ├── __init__.py

# Option B (Large-scale / enterprise ⭐)
# app/
# ├── main.py          # entrypoint only
# ├── core/
# │   └── app.py       # create_app() lives here

# -----------------------------------------------

# Clean imports (re-exporting)
"""
# app/api/__init__.py
from .routes import router

# Now you can do:
from app.api import router
"""
# -----------------------------------------------

# Constants / metadata (lightweight only)
"""
# app/__init__.py
__version__ = "1.0.0"
"""

# -----------------------------------------------

# Optional: aggregation layer
"""
# app/services/__init__.py
from .user_service import UserService
from .auth_service import AuthService
"""

# -----------------------------------------------

# Avoid putting:

# ❌ FastAPI app instance
# ❌ Database connections
# ❌ Route definitions
# ❌ Heavy logic
# ❌ Startup events
