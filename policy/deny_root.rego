package main

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.securityContext.runAsNonRoot == true
  msg = sprintf("❌ Le pod '%v' doit être configuré avec runAsNonRoot: true (ne pas tourner en root)", [container.name])
}
