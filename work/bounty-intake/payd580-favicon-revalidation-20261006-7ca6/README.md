# PayD frontend image: revalidate the fixed-name favicon

The existing contributor Nginx configuration gives every matching `.ico` URL a one-year immutable cache policy. The same contributor tree's HTML explicitly requests `/favicon.ico`, and its public directory contains that fixed-name icon. This source continuation gives that one observed path an exact location with revalidation headers. The existing hashed-asset regex, HTML policy and SPA routing are unchanged.

## Source, contributor and actual consumer chain

Canonical issue: https://github.com/Protocol-Guild/PayD/issues/539  
Existing contributor PR: https://github.com/Protocol-Guild/PayD/pull/580  
Donor repository: `waterWang/PayD`  
Donor branch: `feat/frontend-dockerfile-539`  
Observed immutable head: `9bac1a156b6cd0698d324fcb7e23df902060d54d`  
Changed production path: `frontend/nginx.conf`

Current native metadata observed the PR open and unmerged, with three added files and no PR issue/review comments. Issue 539 was open and unassigned. Both returned issue comments were read: waterWang states the existing Dockerfile work, and shobhamerabacha-star separately requests assignment. Keep that original contribution and both requests distinct from assignment, acceptance or permission to alter upstream. No upstream branch, issue, PR, deployment or account was changed.

| Exact donor object | Git blob | UTF-8 bytes |
|---|---|---:|
| Original frontend/nginx.conf | `78643b41975703319c2be945375f9c6949366b91` | 830 |
| Prepared frontend/nginx.conf | `f0b294aad994a298a21276e3cb942e385414d4d3` | 990 |
| frontend/Dockerfile | `ebacc1b8b8f500068f6858c1d620f232672e4849` | 1125 |
| frontend/.dockerignore | `1d50b0f6af9b68d1a2b30c22d91ad58673a77271` | 103 |
| frontend/vite.config.ts | `f3172629e16b56c809d301bd21aebfc3c8dbb8d8` | 946 |
| frontend/index.html | `51bbb22ad40a994c5c35c9c0b1647284e4246fee` | 869 |
| frontend/package.json | `33e58d67eca11b200b6988835b1f8450f179d2c2` | 2534 |
| root LICENSE | `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | 11357 |

Every complete text above matched its returned provider blob and an independent full Git blob identity. The favicon itself was not read or modified: the complete `frontend/public` directory metadata returned only `favicon.ico`, Git blob `4f17c94a834735ea04cf72bff9589bf3f0a8bbcd`, reported size 7,406 bytes. This is a directory metadata identity, not an independent hash or content review of the binary.

The actual Dockerfile runs the manifest's build script and copies `nginx.conf` to `/etc/nginx/conf.d/default.conf`; it copies `/app/dist` to `/usr/share/nginx/html`. The manifest declares `tsc -b && vite build` and Vite `^7.2.6`. The acquired Vite configuration has no `publicDir`, `root`, `base` or output-directory override. The acquired HTML links `/favicon.ico`. These are connected source relationships under the Dockerfile's frontend build context, not evidence that an image was built or deployed.

## Focused change and semantic basis

The patch adds only:

```nginx
    # The public favicon keeps its filename across builds; revalidate it.
    location = /favicon.ico {
        expires -1;
        try_files $uri =404;
    }
```

The exact location inherits the existing server root and takes precedence over the broad case-insensitive extension regex. A successful response for the observed path receives the negative-expiry policy instead of the sibling one-year immutable policy. The existing file-or-404 result is preserved. The rule is deliberately limited to the exact lowercase path used by the acquired HTML.

Primary sources acquired for this new correction:

- Nginx `location` documentation states that an exact URI match terminates location selection: https://nginx.org/en/docs/http/ngx_http_core_module.html#location
- Nginx `expires` documentation maps a negative time to `Cache-Control: no-cache`, for the response codes covered by that directive: https://nginx.org/en/docs/http/ngx_http_headers_module.html#expires
- Vite's public-directory documentation says those files retain their names and are copied as-is to the distribution root: https://vite.dev/guide/assets.html#the-public-directory

This supports revalidation for new responses; `no-cache` is not a no-storage directive. It neither purges already cached immutable responses nor guarantees immediate icon changes in any browser. No HTTP response was generated or observed. The Dockerfile's `nginx:1.27-alpine` and `node:20-alpine` tags were not pulled or resolved to image digests; current documentation is semantic support, not an installed-image compatibility result.

## Validation and limits

The serialized unified patch has one hunk, twelve rows, six insertions and no deletions. Independent forward materialization produces the exact 990-byte postimage; inverse materialization recovers the exact 830-byte preimage. Removing only the recorded insertion reproduces the full original file. The original missing final newline is preserved; no special final-line hunk is necessary because the hunk ends earlier.

The existing gzip settings, asset regex/header block, index.html policy, server root/listen settings and SPA fallback remain byte-for-byte unchanged. This does not establish proper policies for every future public asset, uppercase alias or other unversioned URL. The other asset policy's broad matching remains explicit. Missing-icon responses retain 404 and are not claimed to receive the success-cache directive.

No image build, pull, Nginx configuration check, shell, Vite/TypeScript execution, HTTP request, browser, cache purge, test/fixture, deployment, Helm/Kubernetes change, upstream submission, sponsor acceptance or reward action was performed. Image size, whole-build success, SPA behavior in a running server, frontend API environment wiring and the rest of issue 539 remain unresolved by this source-only packet.

## Artifacts and license

`favicon-revalidation.patch` is the focused patch against the exact contributor head. This guide records its source/consumer evidence and limits. `LICENSE` is the full unchanged Apache-2.0 text from that same head. Preserve waterWang's contribution and original repository authors; no whole-repository relicensing or ownership transfer is asserted. The donor module and icon are not republished.
