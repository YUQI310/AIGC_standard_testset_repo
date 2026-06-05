# Processed Data Directory

This directory stores standardized outputs generated after ingestion, normalization, validation, and compliance routing.

## Intended structure

- `candidate_pool/`: samples currently eligible for downstream evaluation
- `pending_review/`: samples requiring manual review before further use
- `isolation/license/`: samples isolated due to license restrictions or unclear commercial-use status
- `isolation/compliance/`: samples isolated due to content risk precheck hits
- `isolation/corrupted/`: samples isolated due to corruption, decode failure, or other engineering invalidity

## Design note

This repository currently keeps this directory as a structural placeholder.
Actual processed outputs are expected to be generated locally after the pipeline runs on downloaded datasets.

## Routing logic reference

The target subdirectory depends on:
- `commercial_use`
- `restriction_cleared`
- `review_status`
- file validity
- compliance precheck result
