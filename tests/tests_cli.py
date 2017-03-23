import os
import unittest
from subprocess import Popen, PIPE

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPT_DIR = TESTS_DIR.rstrip('tests')
SCRIPT = os.path.join(SCRIPT_DIR, 'make')
BASECMD = ['python', SCRIPT, '--sim']


class TestCLI(unittest.TestCase):

    def test_cannot_split_the_system_in_cluster_and_env(self):
        """Cluster and env are not separated by :"""
        cmd = BASECMD + ['nuraghe_development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'You must specify an available system.')

    def test_too_much_separators(self):
        """Too much : separators"""
        cmd = BASECMD + ['nuraghe:development:srt']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'You must specify an available system.')

    def test_wrong_cluster_and_right_env(self):
        """The user specify a wrong_cluster and right_env"""
        cmd = BASECMD + ['wrong_cluster:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'"wrong_cluster" not found')

    def test_right_cluster_and_wrong_env(self):
        """The user specify a right_cluster and wrong_env"""
        cmd = BASECMD + ['nuraghe:wrong_env']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'"wrong_env" not found')

    def test_wrong_cluster_and_wrong_env(self):
        """The user specify a wrong_cluster and wrong_env"""
        cmd = BASECMD + ['wrong:wrong']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'System "wrong:wrong" not recognized')

    def test_default_nuraghe_station(self):
        """The default nuraghe station is SRT"""
        cmd = BASECMD + ['nuraghe:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=SRT"')

    def test_override_default_nuraghe_station(self):
        """Override the default nuraghe station"""
        cmd = BASECMD + ['nuraghe:development', '--station', 'Noto']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=Noto"')

    def test_default_escs_station(self):
        """The default escs station is Medicina"""
        cmd = BASECMD + ['escs:production']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=Medicina"')

    def test_override_default_escs_station(self):
        """Override the default escs station"""
        cmd = BASECMD + ['escs:development', '--station', 'Noto']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=Noto"')

    def test_default_escs_noto_station(self):
        """The default escs-noto station is Noto"""
        cmd = BASECMD + ['escs-noto:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=Noto"')

    def test_override_default_escs_noto_station(self):
        """Override the default escs-noto station"""
        cmd = BASECMD + ['escs-noto:development', '--station', 'SRT']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'--extra-vars "cdb=SRT"')



if __name__ == '__main__':
    unittest.main()
