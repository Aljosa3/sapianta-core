# PATH: tests/runtime/test_raw_module_writer.py

import pytest
from runtime.raw_module_writer import RawModuleWriter, RawModuleWriterError


def test_fail_when_no_file_markers(tmp_path):
    writer = RawModuleWriter(project_root=str(tmp_path))

    raw = "just some text\nnothing useful here"

    with pytest.raises(RawModuleWriterError, match="No FILE markers"):
        writer.write_from_raw(raw)


def test_fail_when_text_outside_file_blocks(tmp_path):
    writer = RawModuleWriter(project_root=str(tmp_path))

    raw = (
        "hello this should not be here\n"
        "FILE: modules/a.py\n"
        "print('ok')\n"
    )

    with pytest.raises(RawModuleWriterError):
        writer.write_from_raw(raw)


def test_fail_on_duplicate_file_paths(tmp_path):
    writer = RawModuleWriter(project_root=str(tmp_path))

    raw = (
        "FILE: modules/a.py\nprint('1')\n"
        "FILE: modules/a.py\nprint('2')\n"
    )

    with pytest.raises(RawModuleWriterError, match="Duplicate FILE path"):
        writer.write_from_raw(raw)
