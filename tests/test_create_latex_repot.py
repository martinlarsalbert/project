from src.notebook_to_latex import convert_notebook_to_latex
import pytest
import os
import reports

@pytest.fixture
def build_directory(tmpdir):

    directory = os.path.join(str(tmpdir),'report_latex')

    if not os.path.exists(directory):
        os.mkdir(directory)

    yield directory




def test_create_latex_report(build_directory):

    notebook_path = os.path.join(reports.path,'report','01.1.report.ipynb')
    convert_notebook_to_latex(notebook_path=notebook_path, build_directory=build_directory,save_main=True, skip_figures=False)

