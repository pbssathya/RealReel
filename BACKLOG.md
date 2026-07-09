# RealReel Technical Backlog

---

## Version History

| Date | Version | Author | Notes |
|------|---------|--------|------|
| 8 July 2026 | 0.1 | Sathya & ChatGPT | Initial technical backlog created during Foundation review. |

---

## Purpose

This document captures architectural improvements, technical debt,
future refactoring, and engineering ideas that have been intentionally
postponed.

Items in this document are **not bugs**.

They represent ideas that have been evaluated and deliberately deferred
until the appropriate stage of the project.

The goal is to preserve architectural thinking without interrupting
current development.

---

# High Priority

## CORE-001
### Replace Shot with Scene throughout the engine

**Status**
Pending

**Priority**
High

**Reason**

The domain model has evolved from shot-based editing to scene-based
storytelling.

Scenes represent complete storytelling units and align better with
the language of creators.

**Affected Files**

- realreel/core/scene_planner.py
- realreel/core/production_planner.py
- Any remaining Shot references

---

## CORE-002
### Production becomes the central business object

**Status**
Pending

**Priority**
High

**Reason**

AI Providers and Agents should enrich a Production rather than operate
directly on a Project.

Future method signatures should evolve from:

generate_story(project)

to

generate_story(production)

---

## CORE-003
### Separate Planning from Exporting

**Status**
Pending

**Priority**
High

**Reason**

ProductionPlanner should only construct and enrich a Production.

Exporter should handle writing JSON, MP4, subtitles and other
deliverables.

This reinforces the Single Responsibility Principle.

---

# Medium Priority

## CORE-004
### Rename parser.py

**Status**
Pending

**Priority**
Medium

**Proposed Name**

project_loader.py

**Reason**

The file loads a Project from storage.

It does not parse project contents.

---

## CORE-005
### Add Type Hints

**Status**
Pending

**Priority**
Medium

**Reason**

Improve IDE support, readability and contributor experience.

Example:

def generate_story(
    production: Production
) -> Production

---

## CORE-006
### Remove Hardcoded Paths

**Status**
Pending

**Priority**
Medium

**Reason**

Replace fixed paths with configuration-driven locations to better support
cloud deployment and multiple workspaces.

---

## CORE-007
### Strengthen Provider Interfaces

**Status**
Pending

**Priority**
Medium

**Reason**

Provider interfaces should eventually use Production instead of Project
and return strongly typed objects.

---

# Low Priority

## CORE-008
### Introduce Capability Enumeration

Example

- STORY
- IMAGE
- VOICE
- MUSIC
- SUBTITLE
- TRANSLATION
- REVIEW

This will simplify ProviderManager and improve extensibility.

---

## CORE-009
### Replace History Strings with Production Events

Current

history.append("Scene Added")

Future

ProductionEvent(
    type="SceneAdded",
    timestamp=...
)

This will provide richer auditing and workflow tracking.

---

## CORE-010
### Add Comprehensive Type Checking

Introduce full type annotations across the engine once the domain model
is stable.

---

# Future Ideas

These are intentionally left for later exploration.

- Plugin architecture
- Workflow templates
- Custom AI pipelines
- Multi-language production workflows
- Distributed rendering
- Cloud rendering workers
- Marketplace for templates
- Marketplace for providers
- Visual workflow designer
- RealReel Project Format (.rrp)
- RealReel Production Specification
- Benchmark datasets for creative AI workflows

---

# Review Policy

Every backlog item should satisfy at least one of the following:

- Improves architecture
- Simplifies user experience
- Improves maintainability
- Removes technical debt
- Enables future capabilities

If none of the above apply, the item should not be added.

---

*"Good software is not built by remembering every idea.*

*It is built by recording good ideas until the right time arrives."*
