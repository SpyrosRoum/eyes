from litestar import Litestar, get, Response

@get("/")
async def exists(domain: str) -> Response[str]:
    if domain in known_domains:
        status = 200
    else:
        status = 404

    return Response(domain, status_code=status)

with open("/prefixes.txt", "r") as f:
    lines = f.readlines()

prefixes = [l.strip() for l in lines if len(l.strip()) > 0]
known_domains = list(map(lambda pre: f"{pre}.spyrosr.xyz", prefixes)) + ["spyrosr.xyz"]

app = Litestar(route_handlers=[exists])

