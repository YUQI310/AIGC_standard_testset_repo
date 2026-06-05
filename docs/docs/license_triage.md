# License Triage Notes

## Purpose
This document records the current license routing logic for the first-round datasets in the AIGC standard testset project.

## Routing Principles
- `commercial_use = allowed`: may enter candidate evaluation flow after validation
- `commercial_use = restricted`: send to `pending_review`
- `commercial_use = forbidden`: send to `isolation/license`
- `commercial_use = unknown`: send to `isolation/license` until clarified

## Dataset-Level Notes

### HC3
- License: CC-BY-SA-4.0
- Current assessment: `restricted`
- Reason: commercial use is not absolutely prohibited, but attribution and share-alike obligations require manual review
- Default route: `pending_review`

### GenImage
- Current assessment: `forbidden`
- Reason: non-commercial restriction
- Default route: `isolation/license`

### DFDC
- Current assessment: `unknown`
- Reason: auditable commercial authorization basis is currently unavailable
- Default route: `isolation/license`

### FaceForensics++
- Current assessment: `forbidden`
- Reason: limited to non-commercial research and education
- Default route: `isolation/license`

### Celeb-DF
- Current assessment: `forbidden`
- Reason: non-commercial research only; redistribution restricted
- Default route: `isolation/license`

### FakeAVCeleb
- Current assessment: `forbidden`
- Reason: non-commercial research/education only; redistribution restricted
- Default route: `isolation/license`

## Review Reminder
All restricted or unclear-license datasets require auditable review records before any downstream inclusion decision.
