# RealReel Domain Model

> **Defining the language and business objects of the RealReel production engine.**

---

# Document Information

| Field | Value |
|-------|-------|
| Document | DOMAIN_MODEL |
| Version | 0.2 |
| Status | Draft |
| Created | 3 July 2026 |
| Last Updated | 7 July 2026 |
| Project | RealReel |
| Maintainer | Sathya |

---

# Purpose

This document defines the core business objects of RealReel.

It establishes the common language used throughout the project and serves as the foundation for the engine's architecture and implementation.

The domain model remains independent of:

- AI Providers
- User Interface
- Storage
- Cloud Infrastructure
- Rendering Technology

---

# Version History

| Version | Date | Author | Summary |
|----------|-------------|-------------------|----------------------------------------------|
| 0.2 | 7 July 2026 | Sathya & ChatGPT | Documentation audit and expansion of the production domain model. |
| 0.1 | 3 July 2026 | Sathya | Initial domain model. |

---

# Workspace

A Workspace represents a creator or an organisation.

It is the highest-level container within RealReel.

A Workspace owns:

- Profiles
- Projects
- Templates
- Settings
- Provider Configuration

---

# Project

A Project represents a single creative work.

Examples include:

- FIFA Daily Predictions
- History Shorts
- WhatsApp Tips

A Project owns:

- Brief
- Production
- Assets
- Deliverables
- Logs

A Project has a unique identity throughout its lifecycle.

---

# Brief

A Brief represents the creator's intent.

A Brief may originate from:

- Markdown
- PDF
- DOCX
- Voice Recording
- Chat Conversation

Every creative workflow begins with a Brief.

---

# Production

Production is the heart of RealReel.

It represents the evolving creative work as it moves through the production workflow.

Typical lifecycle:

```
Brief
   │
   ▼
Creative Structure
   │
   ▼
Story
   │
   ▼
Scenes
   │
   ▼
Narration
   │
   ▼
Visual Plan
   │
   ▼
Timeline
   │
   ▼
Render
   │
   ▼
Deliverables
```

Every AI Agent enriches the Production.

The Production itself never knows which AI Provider produced the content.

---

# Scene

A Scene is the smallest storytelling unit within a Production.

A Scene may contain:

- Narration
- Visual Description
- Image Prompt
- Camera Direction
- Emotion
- Transition
- Duration
- Timing

Scenes are independent building blocks.

Together they form a complete Production.

---

# Asset

An Asset represents any reusable creative resource.

Examples include:

- Image
- Video
- Audio
- Music
- Prompt
- Avatar
- Subtitle
- Voice
- Logo

Assets may be supplied by the creator or generated during production.

---

# Timeline

A Timeline defines the sequencing of a Production.

Responsibilities include:

- Ordering
- Timing
- Synchronisation
- Transitions

The Timeline contains no AI logic.

---

# Deliverable

A Deliverable represents content prepared for publication or distribution.

Examples include:

- MP4
- Script
- Production JSON
- Thumbnail
- Subtitle (SRT)
- ZIP Package

Deliverables are the final outputs presented to the creator.

---

# AI Agents

AI Agents enrich a Production.

Examples:

- Story Agent
- Image Agent
- Voice Agent
- Music Agent
- Subtitle Agent
- Timeline Agent

Agents never communicate directly with each other.

Each Agent reads from and contributes to the Production.

---

# AI Providers

Providers supply intelligence to the Agents.

Examples include:

- Ollama
- OpenAI
- Gemini
- Anthropic

Providers never modify Projects directly.

They simply respond to requests made by AI Agents.

---

# Guiding Principle

The creator provides ideas.

RealReel orchestrates the production workflow.

AI Providers contribute intelligence.

These responsibilities remain intentionally separate to preserve flexibility, extensibility, and provider independence.

---

# Related Documents

- README.md
- ARCHITECTURE.md
- ROADMAP.md
- PRINCIPLES.md *(Coming Soon)*

---

*This document is a living part of the RealReel project and evolves alongside the software. Significant updates are recorded in the Version History above.*
