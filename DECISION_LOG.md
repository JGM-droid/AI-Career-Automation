# Decision Log

## Accepted Decisions

### 2026-06-11 - Backend Framework

**Decision:** Use FastAPI for the backend.

**Status:** Final. Do not revisit FastAPI versus Flask.

### 2026-06-11 - Frontend Framework

**Decision:** Use Streamlit for the frontend.

**Status:** Final. Do not revisit Streamlit versus React.

### 2026-06-11 - AI Provider

**Decision:** Use OpenAI as the AI provider.

**Status:** Final. Do not revisit OpenAI versus Anthropic.

### Existing Project Direction - Integration Before AI

**Decision:** Complete the local frontend-to-backend workflow before adding the
OpenAI analysis layer.

**Reason:** The repository already has both application shells, and integration
is the smallest testable step toward a working product.

### Existing Project Direction - Text Resume First

**Decision:** Support `.txt` resume processing before PDF and DOCX parsing.

**Reason:** Plain text validates the workflow without introducing document
parsing complexity.

### Existing Project Direction - Defer Automation Infrastructure

**Decision:** Defer browser automation, job scraping, deployment, CI/CD,
authentication, vector databases, and multi-agent orchestration until the core
analysis workflow is stable.

**Reason:** These capabilities do not advance the current foundation milestone.

## Implementation Notes

- Current backend analysis is intentionally rule-based scaffolding.
- OpenAI integration is planned after the end-to-end request flow works.
- Major architecture changes should be considered only when a milestone is
  complete or the current design blocks progress.
