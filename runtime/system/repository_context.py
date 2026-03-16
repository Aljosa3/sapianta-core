from pathlib import Path


class RepositoryContextBuilder:

    """
    Builds repository context for architecture reasoning.

    Provides:
    - repository structure
    - allowed mutation paths
    - forbidden paths
    """

    def __init__(self, root_path="runtime"):

        self.root = Path(root_path)

    def build_tree(self):

        tree = []

        for p in self.root.rglob("*"):

            if p.is_file():

                tree.append(str(p))

        return tree

    def summarize(self, allowed_paths, forbidden_paths):

        files = self.build_tree()

        summary = []

        summary.append("Repository files:")

        for f in files[:200]:
            summary.append(f)

        summary.append("\nAllowed mutation paths:")

        for a in allowed_paths:
            summary.append(a)

        summary.append("\nForbidden mutation paths:")

        for f in forbidden_paths:
            summary.append(f)

        return "\n".join(summary)