import os
import unittest
from subprocess import Popen, PIPE

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPT_DIR = os.path.dirname(TESTS_DIR)
SCRIPT = os.path.join(SCRIPT_DIR, 'build')
BASECMD = ['python', SCRIPT, '--sim']


class TestCLI(unittest.TestCase):

    def test_cannot_split_the_system_in_cluster_and_env(self):
        """Cluster and env are not separated by :"""
        cmd = BASECMD + ['large_development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'You must specify an available system.')

    def test_too_much_separators(self):
        """Too much : separators"""
        cmd = BASECMD + ['large:development:srt']
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
        cmd = BASECMD + ['large:wrong_env']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'"wrong_env" not found')

    def test_wrong_cluster_and_wrong_env(self):
        """The user specify a wrong_cluster and wrong_env"""
        cmd = BASECMD + ['wrong:wrong']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'System "wrong:wrong" not recognized')

    def test_no_deploy(self):
        """Do not set the tag 'deploy'"""
        cmd = BASECMD + ['small:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertNotRegexpMatches(out, b'branch')
        self.assertNotRegexpMatches(out, b'--tags')

    def test_deploy_branch(self):
        """Set the tag 'deploy'"""
        cmd = BASECMD + ['large:development', '--deploy', 'srt-0.1']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'branch=srt-0.1')
        self.assertRegexpMatches(out, b'--tags deploy')

    def test_deploy_master_no_station(self):
        """Require the station in case of master branch"""
        cmd = BASECMD + ['large:development', '--deploy', 'master']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'--station is required')

    def test_deploy_master(self):
        """Set the station"""
        cmd = BASECMD + [
            'small:development',
            '--deploy',
            'master',
            '--station', 'srt']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'station=srt')

    def test_only_master_accepts_station(self):
        """You can not set the -s if the branch is not master."""
        cmd = BASECMD + [
            'large:development',
            '--deploy',
            'srt-0.1',
            '--station',
            'medicina']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(err, b'only master branch accepts the -s')

    def test_do_not_call_vagrant_up(self):
        """Do not run 'vagrant up' in production."""
        cmd = BASECMD + ['ms:production']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertNotRegexpMatches(out, b'vagrant up')

    def test_vagrant_up_large(self):
        """Run 'vagrant up manager ms as'"""
        cmd = BASECMD + ['large:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'vagrant up manager as ms')

    def test_vagrant_up_ms(self):
        """Run 'vagrant up ms'."""
        cmd = BASECMD + ['ms:development']
        pipes = Popen(cmd, stdout=PIPE, stderr=PIPE)
        out, err = pipes.communicate()
        self.assertRegexpMatches(out, b'vagrant up ms')


if __name__ == '__main__':
    unittest.main()
