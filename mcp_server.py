# -*- coding: utf-8 -*-
import sys, json
from client import GenParkAgentCryptographicAuditTrailMerkleSealer

sealer = GenParkAgentCryptographicAuditTrailMerkleSealer()

def run_tool(name, args):
    if name == "record_event":
        actor = args.get("actor", "agent")
        action = args.get("action", "execute_step")
        details = args.get("details", {})
        return sealer.record_event(actor, action, details)
    elif name == "compute_merkle_root":
        return {"merkle_root": sealer.compute_merkle_root(), "total_events": len(sealer.leaves)}
    elif name == "generate_inclusion_proof":
        idx = int(args.get("index", 0))
        return sealer.generate_inclusion_proof(idx)
    elif name == "verify_proof":
        leaf = args.get("leaf_hash", "")
        proof = args.get("proof_path", [])
        root = args.get("expected_root", "")
        valid = GenParkAgentCryptographicAuditTrailMerkleSealer.verify_proof(leaf, proof, root)
        return {"is_valid": valid}
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Merkle Audit Trail Sealer Self-Test...")
        sealer.record_event("agent_alpha", "login", {"status": "success"})
        sealer.record_event("agent_alpha", "db_query", {"query": "SELECT *"})
        root = sealer.compute_merkle_root()
        assert len(root) == 64
        proof = sealer.generate_inclusion_proof(0)
        valid = GenParkAgentCryptographicAuditTrailMerkleSealer.verify_proof(proof["leaf_hash"], proof["proof_path"], root)
        assert valid is True, "Proof should cryptographically verify"
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
