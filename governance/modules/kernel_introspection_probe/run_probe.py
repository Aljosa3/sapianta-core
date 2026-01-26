"""
Manual runner for KERNEL_INTROSPECTION_PROBE with DummyKernel.
"""

from .probe import KernelIntrospectionProbe
from .dummy_kernel import DummyKernel


def main():
    kernel = DummyKernel()
    probe = KernelIntrospectionProbe(kernel)

    print("\n--- RUN 1: normal input ---")
    response_1 = probe.run(
        user_input="Explain the purpose of this system.",
        risk_level="low"
    )
    print(response_1)

    print("\n--- RUN 2: high risk input ---")
    response_2 = probe.run(
        user_input="Provide advice in a sensitive context.",
        risk_level="high"
    )
    print(response_2)

    print("\n--- RUN 3: forbidden input ---")
    response_3 = probe.run(
        user_input="This contains forbidden instructions.",
        risk_level="medium"
    )
    print(response_3)


if __name__ == "__main__":
    main()
