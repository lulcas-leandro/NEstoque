#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

docker compose -f docker-compose.aws.yml up -d --build
docker compose -f docker-compose.aws.yml exec web flask db upgrade
