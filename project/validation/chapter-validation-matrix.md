# Chapter 1–19 Technical Validation Matrix

**Design authority:** Approved Phase 5 — Repository and Technical Validation Plan (7 November 2026)
**Architecture authority:** Approved Phase 2 — 6 Parts / 19 Chapters
**Research authority:** Approved Phase 3 Research Plan
**Editorial authority:** Approved Phase 4 Editorial Style Guide
**Execution status:** **Designed, not tested**
**Phase 7 Lab Validation:** **Not started**

> **Important boundary:** This file is a public-safe test-design document, not a lab authorization, test report, or claim that any chapter has passed. No lab has been executed by this matrix. DEC-009 (host feasibility preflight) and DEC-010 (Fedora guest/VM profile) remain **Deferred**. Do not inspect the host, select a guest, provision/boot a VM, or execute privileged commands while those decisions remain Deferred. Actual tests require separate Project Owner authorization and an approved disposable environment.

## 1. Status and safety rules

| Status | Meaning |
|---|---|
| **Designed, not tested** | Objective, method, evidence and acceptance criteria are defined; no execution result is claimed. |
| **Verification Required** | A kernel/API/tool/version/platform detail must be checked against the exact selected release. |
| **Blocked** | A required prerequisite or approval is unavailable. Record the blocker; do not silently skip it. |
| **PASS** | Every acceptance criterion is met, evidence is present, and cleanup succeeds. |
| **FAIL** | Required behavior is incorrect, evidence contradicts expectation, a safety invariant is violated, or cleanup leaves residue. |
| **UNRESOLVED** | Test cannot be run or evidence is insufficient/ambiguous. UNRESOLVED is not PASS. |

### Common evidence requirements

A future authorized record should identify the chapter/test ID, source commit or document revision, exact software/kernel/specification versions, environment baseline reference, privilege level, exact commands/configuration, redacted actual output, expected-versus-actual result, PASS/FAIL/BLOCKED/UNRESOLVED rationale, cleanup evidence, limitations and reviewer. Personal identifiers and private host details must stay in private records and must not be committed to this public repository.

### Common safety requirements

- Any privileged, namespace, mount, cgroup, firewall, runtime-daemon or kernel-facing experiment must take place only in a separately authorized disposable environment after the required feasibility and VM decisions are approved.
- Do not run privileged container experiments on an everyday host. Do not expose host paths, host Docker/container sockets, credentials, SSH material or private host data to a guest or container.
- Keep SELinux Enforcing; never disable it as a routine workaround.
- Use only dedicated test processes, directories, namespaces, cgroups, sockets, bridges and firewall tables. Do not modify system-managed resources.
- Record cleanup/rollback success. If cleanup is uncertain, stop and preserve the environment for review rather than improvising destructive cleanup.
- `project/` is outside the MkDocs `docs/` directory but remains visible in this public GitHub repository. Publish only sanitized, public-safe design records and blank templates.

## 2. Chapter-by-chapter validation design

### Chapter 1 — Understanding Containers

- **Objective:** Confirm that a container is explained as an isolated process environment, distinguish it from a VM, and accurately describe shared-kernel behavior.
- **Environment / privilege / risk:** Fedora Linux or a future approved disposable Fedora VM; `ps`, `pstree`, procfs. Normal-user read-only inspection; no root required for conceptual comparison. **Low**.
- **Method:** Inspect process tree and `/proc`; where a safe pre-existing test container is available under separate authorization, compare process metadata; review the architecture diagram and explain the kernel relationship.
- **Expected evidence:** Sanitized process tree and `/proc` excerpts, diagram review notes, and a short explanation distinguishing guest kernel from shared host kernel.
- **Acceptance:** Correctly distinguish image from running process, container from VM, and explain why `chroot` alone is not a complete container security boundary. No claim of total isolation.
- **Cleanup:** Remove only temporary examples; stop only a test-owned demonstration container.
- **Limitations / gaps:** Visibility depends on namespaces and runtime configuration. One process listing does not prove security isolation.
- **Status:** Designed, not tested.

### Chapter 2 — Linux Processes and System Calls

- **Objective:** Verify explanations of parent/child lifecycle, `fork()`, `clone()`, `execve()`, `wait()`, zombie/orphan states and PID 1 behavior.
- **Environment / privilege / risk:** Fedora Linux, shell, procfs, `ps`, `pstree`; reviewed sample program. Normal user for ordinary process tests; any namespace-specific PID 1 demonstration would require a separately approved disposable VM and appropriate privilege. **Low** for user-owned processes; **Medium** for namespace/root tests.
- **Method:** Inspect PID/PPID and `/proc/<PID>/status`; run a controlled parent/child example; verify child reaping and exit status. Verify `clone3()` kernel support separately from availability of a userspace/libc wrapper.
- **Expected evidence:** Reviewed source, command transcript, PID/PPID observations, exit status and reaping/cleanup record.
- **Acceptance:** Distinguish `execve()` replacement from process creation; observe zombie state only in a controlled test and reap it; leave no child process behind.
- **Cleanup:** Parent reaps children; terminate only test-owned processes; remove temporary source and binaries.
- **Limitations / gaps:** `clone3()` kernel support and wrapper availability differ; exact kernel/libc behavior is version-specific.
- **Status:** Designed, not tested; `clone3()` detail requires verification.

### Chapter 3 — Linux Namespaces

- **Objective:** Validate the approved set of exactly eight Linux namespace types: PID, mount, network, UTS, IPC, user, cgroup and time; explain `clone()`, `unshare()` and `setns()` roles.
- **Environment / privilege / risk:** Future approved disposable Fedora VM; `lsns`, procfs and util-linux. Normal user for read-only inspection; root or narrowly scoped namespace permissions only inside the approved VM. **Medium**, rising to **High** for mount/network modifications.
- **Method:** Inspect `/proc/<PID>/ns/`, compare namespace identifiers, and use selected PID/UTS/network/mount namespace examples. Check all eight types against kernel documentation and actual selected-kernel support.
- **Expected evidence:** Namespace identifiers, sanitized `lsns` output, process behavior observations and exact kernel version.
- **Acceptance:** Book content lists exactly eight types; every demonstrated type has a reproducible observation; unsupported features are explicitly marked unavailable, not fabricated.
- **Cleanup:** Terminate test processes, exit namespace shells, unmount test mounts and remove temporary namespace references.
- **Limitations / gaps:** Availability and privilege requirements vary by kernel configuration, distribution policy and user-namespace settings.
- **Status:** Designed, not tested; per-type availability requires verification.

### Chapter 4 — Control Groups (cgroups)

- **Objective:** Verify cgroups v2 hierarchy, controller availability, delegation and CPU/memory/PID controls.
- **Environment / privilege / risk:** Future approved disposable Fedora VM with cgroup v2 mounted and required controllers available/delegated. Root inside the VM or a properly delegated subtree for writes; normal user for read-only inspection. **Low** for inspection; **High** for modifying cgroups.
- **Method:** Inspect `findmnt -t cgroup2`, `cgroup.controllers` and `cgroup.subtree_control`; test `cpu.max`, `memory.max` and `pids.max` only in a dedicated subtree; observe counters/events.
- **Expected evidence:** Before/after cgroup tree, controller files, test-process membership, configured limits, observed resource behavior and cleanup record.
- **Acceptance:** Test process is confined to the dedicated subtree; configured limits appear in kernel files and observed behavior matches controller semantics; host/system cgroups remain unchanged.
- **Cleanup:** Stop and reap test processes, remove only the test subtree as permitted, and confirm no process remains and no systemd-managed group was altered.
- **Limitations / gaps:** Controller availability, delegation and systemd ownership vary; I/O demonstrations may require a suitable device/filesystem.
- **Status:** Designed, not tested; exact controller availability requires verification.

### Chapter 5 — Linux Capabilities and Privilege Model

- **Objective:** Inspect and explain effective, permitted, inheritable, bounding and ambient capability sets, and `no_new_privs`.
- **Environment / privilege / risk:** Future approved Fedora VM, procfs, `capsh` or equivalent if installed, and a small safe test program. Normal user for inspection; root only inside the disposable VM for controlled setup. **Medium**.
- **Method:** Read `CapInh`, `CapPrm`, `CapEff`, `CapBnd` and `CapAmb` from `/proc/<PID>/status`; inspect `no_new_privs`; test one narrowly selected operation in an expendable process.
- **Expected evidence:** Before/after capability sets, test operation result, process exit status and exact kernel/tool versions.
- **Acceptance:** Capability sets are identified correctly; privilege reduction causes the expected operation to fail without affecting unrelated processes; `no_new_privs` behavior is accurately described.
- **Cleanup:** Terminate the test process; do not leave altered capabilities on persistent binaries or system services.
- **Limitations / gaps:** Capability checks depend on user namespace, filesystem and operation context; one syscall result does not prove a complete privilege boundary.
- **Status:** Designed, not tested; operation-specific capability mapping requires verification.

### Chapter 6 — Container Filesystem Isolation

- **Objective:** Validate temporary rootfs setup, mount namespaces, bind mounts, mount propagation and `pivot_root()` behavior.
- **Environment / privilege / risk:** Future approved disposable Fedora VM, dedicated temporary rootfs/filesystem, mount tools and procfs. Root only inside the VM for mount and `pivot_root()` operations. **High**.
- **Method:** Inspect `/proc/self/mountinfo` and `findmnt`; create a mount namespace; test bind mounts and propagation; verify `pivot_root()` preconditions, old-root detachment and path handling inside the VM.
- **Expected evidence:** Mount tables before/after, namespace identifiers, root path observed by the test process and cleanup transcript.
- **Acceptance:** Test process sees only intended rootfs mounts; old root is not reachable through unintended paths; no host filesystem path is exposed; cleanup completes.
- **Cleanup:** Exit test namespace/process, unmount in reverse dependency order, remove temporary rootfs and verify no mount remains.
- **Limitations / gaps:** Mount API behavior, SELinux labels, filesystem support and propagation defaults vary; exact syscall ordering requires implementation review.
- **Status:** Designed, not tested; `pivot_root()` sequence requires verification.

### Chapter 7 — OverlayFS and Container Image Storage

- **Objective:** Distinguish OCI image layers, OverlayFS lower/upper/work/merged directories, writable layers, storage drivers and snapshotter abstractions.
- **Environment / privilege / risk:** Future approved disposable Fedora VM with OverlayFS support and temporary directories on a compatible backing filesystem. Root inside the VM for OverlayFS mounts; normal user for exported image metadata. **Medium** for read-only inspection; **High** for mounts/storage changes.
- **Method:** Mount lower/upper/work/merged directories; read a lower-layer file, modify it through merged and inspect copy-up in upper; examine delete/whiteout behavior where exposed; inspect OCI layer metadata and a selected engine/containerd snapshotter separately.
- **Expected evidence:** Mount command/options, directory listings, file hashes/content before/after, layer descriptor/digest information and driver/snapshotter identity.
- **Acceptance:** Explain OCI layers separately from OverlayFS directories; demonstrate copy-up; identify writable state per implementation; describe snapshotter as an abstraction/backend, not as a synonym for OverlayFS.
- **Cleanup:** Unmount merged filesystem, ensure no users remain, then remove only temporary test directories. Do not modify production engine storage.
- **Limitations / gaps:** Kernel and backing-filesystem features affect OverlayFS options; engine storage layouts differ and not all snapshotters use OverlayFS.
- **Status:** Designed, not tested; backing-filesystem compatibility requires verification.

### Chapter 8 — Container Networking Internals

- **Objective:** Trace isolated packet flow and validate veth/bridge/routing/NAT, DNS and troubleshooting concepts.
- **Environment / privilege / risk:** Future approved disposable Fedora VM; `iproute2`, `tcpdump`, `nftables` and DNS utilities; isolated/disconnected test network. Root inside VM for interface/route/firewall writes; normal user for read-only checks. **Medium** for namespace-only tests; **High** for firewall/routing changes.
- **Method:** Create test namespaces/veth/bridge; inspect `ip addr`, `ip route`, `ss` and `nft list ruleset`; capture packets; test DNS only in an explicitly configured test environment.
- **Expected evidence:** Topology diagram, interface/address/route tables, test-specific firewall rules, packet captures and DNS query/result.
- **Acceptance:** Trace packet path hop by hop; routing/NAT behavior matches configured rules; distinguish DNS failure from routing/firewall failure; host firewall state remains unchanged.
- **Cleanup:** Remove test namespaces, veth pairs, bridges, routes and only the test-specific firewall table/chain; verify removal.
- **Limitations / gaps:** DNS depends on resolver setup; offload may alter captures; external connectivity is not required for isolated tests.
- **Status:** Designed, not tested; Fedora firewall backend and resolver behavior require verification.

### Chapter 9 — OCI Image Specification

- **Objective:** Verify OCI image index, manifest, config, layers, descriptors, digests and DiffIDs against a selected specification version.
- **Environment / privilege / risk:** Local OCI image layout or locally available image plus JSON tools; core inspection requires no registry/network. Normal user. **Low**.
- **Method:** Inspect `oci-layout`, `index.json`, manifest/config and layer descriptors; verify digest calculations against the pinned specification; compare compressed digest with uncompressed DiffID.
- **Expected evidence:** Sanitized JSON excerpts, media types, digest checks and platform-selection example.
- **Acceptance:** Identify fields against the pinned Image Specification; Chapter 8 networking is not a prerequisite; do not confuse image config/layer descriptors with runtime `config.json`.
- **Cleanup:** Remove only temporary extracted image/layout files.
- **Limitations / gaps:** Media types, artifact use and tooling support vary by specification/tool version; registry behavior is outside the local-layout core test.
- **Status:** Designed, not tested; exact image-spec release and tool behavior require verification.

### Chapter 10 — OCI Runtime Specification

- **Objective:** Verify OCI bundle, `config.json`, rootfs/process/namespace/mount/resource fields and lifecycle semantics.
- **Environment / privilege / risk:** Future approved disposable Fedora VM, pinned OCI runtime, minimal prepared rootfs and bundle. Normal user for static schema review; root only inside VM for runtime execution. **Low** for static JSON review; **High** for execution/mount/cgroup changes.
- **Method:** Validate config against the pinned specification/schema where available; use a test runtime for `create`/`start`/`state`/`kill`/`delete`; inspect namespaces, mounts and cgroups.
- **Expected evidence:** Bundle files, `ociVersion`, runtime state output, process status and cleanup record.
- **Acceptance:** Distinguish spec-defined fields from runtime-specific behavior; lifecycle matches the selected implementation/spec version; teardown leaves no test process/resource.
- **Cleanup:** Delete test container, stop processes, unmount rootfs and remove test cgroup/state.
- **Limitations / gaps:** Runtime implementations differ in optional fields/hooks; schema validation alone does not prove runtime behavior.
- **Status:** Designed, not tested; OCI/runtime compatibility requires verification.

### Chapter 11 — runc and crun

- **Objective:** Compare observable OCI execution behavior of runc and crun using the same bundle.
- **Environment / privilege / risk:** Future approved disposable Fedora VM, pinned runc/crun versions, same prepared rootfs and OCI bundle. Root inside VM for normal runtime labs; rootless tests are optional and require separate scope approval. **High**.
- **Method:** Execute equivalent bundle with each runtime; inspect runtime state, process tree, namespace IDs, mounts, cgroups and cleanup; compare only equivalent configurations.
- **Expected evidence:** Runtime versions, bundle hash, command logs, state output, process/namespace/cgroup evidence and cleanup results.
- **Acceptance:** Separate common OCI behavior from implementation-specific behavior; tie differences to exact versions/configuration; make no performance-superiority claim without a controlled benchmark.
- **Cleanup:** Remove each test container and associated process, mounts, cgroups and state before the next run.
- **Limitations / gaps:** Features, defaults and optional OCI fields vary by release; this is not a full conformance suite.
- **Status:** Designed, not tested; exact pairwise runtime support requires verification.

### Chapter 12 — containerd and containerd-shim

- **Objective:** Inspect containerd content store, metadata, snapshotter, container/task, shim and daemon-level namespace behavior.
- **Environment / privilege / risk:** Future approved disposable Fedora VM; isolated containerd config/data root/socket and selected runtime. Never reuse system production daemon state. Service/admin privileges only inside VM; normal user for safe read-only queries where permitted. **High** for service/socket/data-root changes.
- **Method:** Use an isolated test daemon/instance; inspect content, snapshot, container and task; inspect shim process; compare containerd logical namespace metadata with Linux namespace identifiers.
- **Expected evidence:** Test daemon config, separate data root/socket, `ctr`/API output, shim process tree, snapshot metadata and Linux namespace IDs.
- **Acceptance:** Explain containerd namespace as daemon-level logical organization, not a kernel namespace or security boundary; distinguish task from container metadata; leave system daemon/data untouched.
- **Cleanup:** Stop test daemon, ensure shim/task exits, delete test content only within isolated data root, and remove test socket/runtime directory.
- **Limitations / gaps:** Runtime v2/shim lifecycle and commands vary across containerd releases; isolated-daemon procedure requires verification.
- **Status:** Designed, not tested; isolated daemon configuration requires verification.

### Chapter 13 — Docker Engine Internals

- **Objective:** Inspect Docker client/API/daemon/containerd/runtime execution path and storage/network integration.
- **Environment / privilege / risk:** Future approved disposable Fedora VM with a chapter-approved Docker Engine version. Do not mount the host Docker socket. Docker admin/root-equivalent access only inside VM; otherwise read-only inspection. **High** because a rootful Docker daemon/API can control its host.
- **Method:** Inspect `docker info`, daemon process, API metadata and runtime process chain; compare image/store/network configuration to the documented release.
- **Expected evidence:** Docker/Engine/containerd/runtime versions, process tree, inspected test-container metadata, and test network/storage records.
- **Acceptance:** Distinguish Docker client, Engine API, `dockerd`, containerd and low-level runtime responsibilities; document socket-exposure risk; expose no host socket or credentials to the guest.
- **Cleanup:** Remove test containers/images/networks/volumes in the VM only; confirm test workload stops.
- **Limitations / gaps:** Architecture and storage integration change by Engine version/configuration; exact pairing must be verified.
- **Status:** Designed, not tested; exact Engine/containerd pairing requires verification.

### Chapter 14 — Container Security Mechanisms

- **Objective:** Examine capabilities, seccomp, SELinux/LSM, device/mount restrictions, socket exposure and image-trust concepts.
- **Environment / privilege / risk:** Future approved disposable Fedora VM with SELinux Enforcing, approved runtime and test-only image/rootfs/profiles. Normal user for policy inspection; root only inside VM for controlled runtime security tests. **Low/Medium** for read-only inspection; **High** for changing policy/profile/device/mount state.
- **Method:** Inspect capability sets, seccomp profile behavior, SELinux labels/audit records, mount flags, device access and socket permissions; analyze image digest/signature/provenance using local artifacts.
- **Expected evidence:** Sanitized policy/profile, `getenforce`, labels, capability sets, allowed/blocked test outcomes and supply-chain metadata.
- **Acceptance:** Demonstrate layered controls and limitations; distinguish digest identity from publisher trust; explain rootful Docker socket and host bind-mount risks without exposing host data; keep SELinux Enforcing.
- **Cleanup:** Stop test containers, remove temporary profiles/rules/mounts and test artifacts; restore VM snapshot if policy state is uncertain.
- **Limitations / gaps:** SELinux/AppArmor availability and policies differ; seccomp depends on architecture/kernel/runtime; signature verification needs a separately pinned trust policy.
- **Status:** Designed, not tested; policy/profile and verification-tool versions require verification.

### Chapter 15 — Rootless Containers

- **Objective:** Inspect rootless Podman process model, user-namespace mapping, storage backend, networking and cgroup constraints.
- **Environment / privilege / risk:** Future approved disposable Fedora VM; non-root test user, subordinate UID/GID configuration if needed, and rootless-capable runtime. Normal user for rootless execution; administrator only inside VM to prepare a disposable test account/mapping. **Medium**, rising to **High** for account mappings or persistent storage changes.
- **Method:** Inspect `/proc/<PID>/uid_map`, `gid_map`, `podman info`, storage backend and network helper; test resource controls only where delegated.
- **Expected evidence:** UID/GID maps, rootless runtime info, storage/network selection, process tree and cgroup behavior.
- **Acceptance:** Explain user-namespace mapping and rootless limitations; do not claim rootless guarantees complete isolation; test files/processes belong only to the disposable test user.
- **Cleanup:** Stop/remove test containers, remove only disposable user data, revert temporary subuid/subgid configuration if added.
- **Limitations / gaps:** Kernel/userns policy, storage backend, network helper and cgroup delegation vary by Fedora/tool version.
- **Status:** Designed, not tested; rootless backend/defaults require verification.

### Chapter 16 — Container Operations and Troubleshooting

- **Objective:** Use `nsenter`, `lsns`, `strace`, `findmnt` and network/runtime tools to troubleshoot controlled failures with evidence.
- **Environment / privilege / risk:** Future approved disposable Fedora VM, diagnostic tools and synthetic test workloads/logs. Normal user for most inspection; root only inside VM where tracing/namespace entry requires it. **Medium**; **High** for privileged namespace entry or tracing sensitive processes.
- **Method:** Reproduce selected process, namespace, mount, DNS/route, resource or startup failure; capture relevant output; follow symptom → evidence → hypothesis → test → fix → verification.
- **Expected evidence:** Sanitized commands/output, trace excerpts, mount/network/cgroup evidence, supported root cause and successful re-test.
- **Acceptance:** Root cause is supported by evidence; diagnostic tool use is appropriate; fix resolves reproduced failure; cleanup restores test state.
- **Cleanup:** Stop workloads, remove temporary files, undo test network/mount/cgroup changes and clear sensitive logs.
- **Limitations / gaps:** `strace` can alter timing and expose arguments/data; namespace entry requires authorization; output varies by version.
- **Status:** Designed, not tested; reproducible failure scenarios require verification.

### Chapter 17 — Podman Internals

- **Objective:** Inspect local daemonless Podman flow and the optional REST service model, including Libpod/conmon/runtime/storage/network relationships.
- **Environment / privilege / risk:** Future approved disposable Fedora VM with pinned Podman release and rootless test user. Normal user for local/rootless inspection; root only inside VM for rootful service tests. **Medium** for rootless; **High** for rootful API service/socket exposure.
- **Method:** Inspect `podman info`, process tree, conmon, configured OCI runtime, storage/network backend; separately start/test/stop `podman system service` only if that optional service topic is in the chapter scope.
- **Expected evidence:** Podman version/config, process tree, service socket permissions, API/service state, runtime and backend records.
- **Acceptance:** Explain daemonless local CLI behavior without claiming that no service exists; distinguish optional API service and its user/root implications; compare Docker only at equivalent scope.
- **Cleanup:** Stop API service/socket activation if started; remove test containers/storage/network and test socket files.
- **Limitations / gaps:** Service model, Netavark and storage defaults vary by release; verify Fedora packaging.
- **Status:** Designed, not tested; service defaults/backend versions require verification.

### Chapter 18 — Kubernetes Container Runtime Architecture

- **Objective:** Verify Kubelet, CRI, containerd/CRI-O, OCI runtime, Pod sandbox/pause and CNI startup responsibilities.
- **Environment / privilege / risk:** Primary validation is documentation/API/source analysis and does not require a live cluster. A disposable cluster is optional only after separate approval. Normal user for documentation/source/diagram review; cluster-admin/node privileges only for optional live-cluster validation. **Low** for documentation review; **High** for live node/runtime changes.
- **Method:** Check versioned Kubernetes CRI docs/API; trace `RunPodSandbox`, container create/start and status flow; compare containerd/CRI-O integration; correctly attribute CNI integration (not a direct Kubelet CNI call).
- **Expected evidence:** Versioned API references, responsibility table, source/document links, startup-sequence diagram and reviewed terminology.
- **Acceptance:** Distinguish Kubelet↔CRI↔runtime responsibilities; do not confuse OCI runtime with CRI; describe pause process as an implementation pattern, not a universal mandate; attribute CNI accurately; preserve the focused 10-page bridge scope.
- **Cleanup:** No cleanup for documentation-only research. Any optional cluster must be disposable and torn down under its own separately approved procedure.
- **Limitations / gaps:** Runtime behavior differs by version/CRI implementation; exact Kubernetes/containerd/CRI-O compatibility pairing requires verification.
- **Status:** Designed, not tested; version pairing requires verification.

### Chapter 19 — Build Your Own Linux Container Runtime in Go

- **Objective:** Validate the educational runtime Core requirements milestone-by-milestone in a separately approved disposable Fedora VM.
- **Environment / privilege / risk:** Requires approved disposable Fedora VM, exact Fedora/kernel/Go versions in baseline, prepared rootfs, cgroups v2, SELinux Enforcing and tested snapshot/rollback. Rootful runtime only inside that VM; normal user for source editing and non-privileged unit tests. **High**.
- **Method:** Follow M0–M8 below; collect helper IPC, namespaces, loopback, rootfs/pivot, cgroups, security, lifecycle, tests and cleanup evidence.
- **Expected evidence:** Sanitized environment baseline, source commit, Go version, configuration, commands/output, process/namespace/cgroup/mount observations, test results, cleanup report and unresolved issues.
- **Acceptance:** Every Core milestone M1–M8 passes after M0 is independently cleared; network-namespace loopback is configured/up; optional userns/veth/bridge/NAT/DNS/CNI/rootless features are not required; no external connectivity is required; no process/mount/cgroup/state leaks remain after normal or failure cleanup.
- **Cleanup:** Use runtime delete/cleanup; verify child processes, mounts, cgroups, temporary network objects and state are gone; revert VM snapshot if cleanup is incomplete.
- **Limitations / gaps:** Educational runtime only. No production security guarantee, full OCI compliance, registry, CNI implementation, general-purpose network stack or rootless parity. Go and kernel process-creation behavior is version-specific.
- **Status:** Designed, not tested; all environment/API/runtime-specific claims require verification before Phase 7.

## 3. Chapter 19 Core and Optional acceptance boundary

### Core requirements

1. Helper-process/re-exec architecture.
2. Parent/helper IPC with explicit bounded communication protocol.
3. Startup handshake and error propagation.
4. Process synchronization, signal handling and child reaping.
5. PID, UTS, mount, IPC and network namespaces.
6. Network Namespace loopback (`lo`) setup and verification.
7. Prepared root filesystem.
8. Required mount setup and `pivot_root()`.
9. Old-root cleanup.
10. cgroups v2 CPU, memory and PID controls.
11. Capability reduction.
12. `no_new_privs`.
13. Narrowly scoped seccomp demonstration.
14. Lifecycle: `create`, `start`, `state`, `kill`, `delete`.
15. Error handling, cleanup and tests.

### Optional extensions — not Core pass requirements

- User Namespace and UID/GID mapping.
- veth, Linux bridge, routing, NAT and port publishing.
- DNS and CNI-related extensions.
- Rootless-runtime parity.

No external network connectivity is required for Core. Optional features must not be treated as blockers to Core acceptance.

## 4. Chapter 19 measurable milestone gates (M0–M8)

> All milestones below are future test design only. With DEC-009 and DEC-010 Deferred, M0 cannot start; M1–M8 remain blocked behind M0. No milestone is PASS, Owner-tested or Independently tested.

| Milestone | Scope and verification | Minimum evidence | PASS condition | Failure / cleanup boundary | Current status |
|---|---|---|---|---|---|
| **M0 — VM preflight and rollback** | Host feasibility, signed Fedora ISO verification, VM boot/install, SELinux, cgroups v2, snapshot/rollback. This requires separate approval to resume DEC-009/010. | Sanitized host/guest baseline, ISO checksum/signature record, `getenforce`, cgroup mount/controllers, snapshot/rollback result. | Host remains responsive; guest boots; SELinux Enforcing; cgroups v2 and required controllers verified; rollback restores baseline. | Fail for host instability, failed ISO verification, non-Enforcing SELinux, missing required baseline without approved alternative, or failed rollback. Revert baseline and remove harmless test change. | **BLOCKED — DEC-009/010 Deferred.** |
| **M1 — Parent/helper communication and process safety** | Re-exec helper; bounded pipe/socket protocol; startup handshake; malformed/oversized input; invalid config; early helper exit; parent cancellation/signals; synchronization and reaping. Verify pinned Go/kernel process-launch behavior. | Protocol description, source/test hash, parent/helper logs, exit codes/timeouts, useful IPC trace, process tree before/after. | Explicit READY/ERROR outcome; malformed input fails safely; errors propagate; cancellation/termination/reaping work; no hung or orphan helper. | Fail for premature success, deadlock without bounded failure, swallowed errors or leaked child. Reap helper, close IPC descriptors and verify no child. | **BLOCKED — M0 prerequisite.** |
| **M2 — Core namespace isolation** | Configure PID, UTS, mount, IPC and network namespaces; inspect `/proc/<PID>/ns/*` and `lsns`; observe PID, hostname, mount, IPC and network views. | Namespace IDs, process tree, hostname/PID/mount observations and kernel version. | All five required namespace types are configured for intended process; observations show intended isolation; host namespace state unchanged. | Fail if a required namespace is absent/shared unexpectedly or host state changes. Terminate processes, reap children and close namespace FDs. | **BLOCKED — M0 prerequisite.** |
| **M3 — Network Namespace and loopback** | Confirm distinct network namespace; inspect with `ip link`/`ip addr`; bring `lo` UP; test `127.0.0.1` using ping if installed or an equivalent socket test. Compare host loopback before/after. | Namespace ID, `ip -details link`/`ip addr`, loopback test and host-before/after record. | Distinct network namespace; `lo` present and UP; loopback succeeds; host networking unchanged; no external connectivity. | Fail if host namespace is shared, loopback stays DOWN, host network changes or optional veth/bridge/NAT is needed. Stop namespace processes and verify host state. | **BLOCKED — M0 prerequisite.** |
| **M4 — Prepared rootfs, mounts and `pivot_root()`** | Validate rootfs/path; apply reviewed mounts in mount namespace; call `pivot_root()`; verify `/`, mountinfo and old-root detachment; test invalid path/symlink/failure handling. | Rootfs manifest/hash, mount tables, helper `/proc/self/mountinfo`, path tests and old-root cleanup log. | Process sees prepared rootfs as `/`; only intended mounts present; old root not unintentionally reachable; no host path exposed; failure cleanup works. | Fail for path escape, reachable old root, host exposure or leaked mounts. Unmount in reverse order; remove rootfs only when unreferenced. | **BLOCKED — M0 prerequisite.** |
| **M5 — cgroups v2 resource controls** | Verify controllers; use only approved delegated subtree; assign test process; set `cpu.max`, `memory.max`, `pids.max`; inspect files/events and bounded workload. | Controller preflight, cgroup path/config, process membership, observed behavior and teardown. | Process confined to dedicated subtree; controls accepted/observable and behavior matches kernel docs; no system cgroup modified. | Fail for system-managed cgroup writes, silently missing controller, escaped process, ineffective limit or failed cleanup. Stop/reap process and remove child hierarchy. | **BLOCKED — M0 prerequisite.** |
| **M6 — Capability and seccomp controls** | Record capabilities; reduce explicit set; enable `no_new_privs`; apply narrowly scoped seccomp filter to a dedicated syscall demo; test allowed and blocked behavior. | Capability sets, `NoNewPrivs`, filter config/hash, allowed/blocked output, architecture/kernel. | Unneeded capabilities absent; `no_new_privs` active; only intended behavior blocked; error is safe/documented; no claim of broad security guarantee. | Fail if privilege remains too broad, cleanup/control breaks unexpectedly, security test is outside VM or SELinux is disabled. Terminate test process; revert snapshot if needed. | **BLOCKED — M0 prerequisite.** |
| **M7 — Lifecycle, signals and cleanup** | Test `create`/`start`/`state`/`kill`/`delete`, invalid transitions, supported signals, helper crash, parent interruption and delete-while-running policy. | State records, command logs, exit/signal results, process tree, mount/cgroup inventory before/after. | Documented transitions work; invalid transitions fail safely; children reaped; normal/failure/interruption paths clean mounts/cgroups/state; repeated delete behavior deterministic. | Fail for stale state, leaked resources, incorrect signals or unrelated-resource deletion. Verify no process/mount/cgroup/state remains; revert snapshot if uncertain. | **BLOCKED — M0 prerequisite.** |
| **M8 — Test suite and repeatability** | Run unit/integration tests from clean snapshot; test malformed IPC/config, invalid ID/path, failed mount, missing controller, helper crash and interrupted cleanup; repeat Core sequence. | Test commands/output, Go test report, source commit/hash, baseline and cleanup checklist. | Required Core tests pass from clean snapshot; failure cases fail safely; no leaks; no optional feature required. | Fail for any Core test failure, cleanup residue or undocumented host dependency. Run cleanup audit and revert snapshot after evidence capture. | **BLOCKED — M0 prerequisite.** |

**Capstone completion meaning:** M0–M8 PASS would validate only the educational implementation under the tested conditions. It does not prove production readiness, adversarial multi-tenant isolation, full OCI compliance or security certification.

## 5. Evidence record template and public/private boundary

For an actual future test, use `project/validation/lab-record-template.md` as a blank structure, then keep detailed evidence privately unless it has been sanitized and approved for public release. Public records may include only necessary non-sensitive versions, test ID, method summary, result and sanitized excerpts. Never publish usernames, hostnames, serial numbers, private IPs, home paths, credentials, tokens, SSH material, raw unredacted logs or personal information.

## 6. Current matrix status summary

- Chapters 1–19: **Designed, not tested**.
- Chapter 19 M0: **Blocked** until DEC-009/010 are separately resumed and resolved.
- Chapter 19 M1–M8: **Blocked** behind M0; no test execution is implied.
- Phase 7 Lab Validation: **Not started**.
- No Owner-tested or Independently-tested lab evidence is published in this repository.
