---
name: genpark-agent-cryptographic-audit-trail-merkle-sealer-skill
description: Agent cryptographic audit trail Merkle sealer with tamper-evident SHA-256 tree generation, logarithmic inclusion proofs, and verifiable integrity checks.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'record_event', 'description': 'Append an agent interaction or tool call to the Merkle audit trail.'}
  - {'name': 'compute_merkle_root', 'description': 'Compute the current cryptographic root hash of all recorded events.'}
  - {'name': 'generate_inclusion_proof', 'description': 'Generate a cryptographic audit proof path for a specific event.'}
  - {'name': 'verify_proof', 'description': 'Verify an inclusion proof against an expected Merkle root.'}
---

# Genpark Agent Cryptographic Audit Trail Merkle Sealer Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Agent Cryptographic Audit Trail Merkle Sealer Skill**.
Your primary directive is to execute: Agent cryptographic audit trail Merkle sealer with tamper-evident SHA-256 tree generation, logarithmic inclusion proofs, and verifiable integrity checks.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'record_event', 'description': 'Append an agent interaction or tool call to the Merkle audit trail.'}`
- `{'name': 'compute_merkle_root', 'description': 'Compute the current cryptographic root hash of all recorded events.'}`
- `{'name': 'generate_inclusion_proof', 'description': 'Generate a cryptographic audit proof path for a specific event.'}`
- `{'name': 'verify_proof', 'description': 'Verify an inclusion proof against an expected Merkle root.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'record_event', 'description': 'Append an agent interaction or tool call to the Merkle audit trail.'}`
- `{'name': 'compute_merkle_root', 'description': 'Compute the current cryptographic root hash of all recorded events.'}`
- `{'name': 'generate_inclusion_proof', 'description': 'Generate a cryptographic audit proof path for a specific event.'}`
- `{'name': 'verify_proof', 'description': 'Verify an inclusion proof against an expected Merkle root.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
