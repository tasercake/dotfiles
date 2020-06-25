#!/usr/bin/env python3
import os
import shutil
import subprocess


class FileSystemOp:
    @abstractmethod
    def validate(self):
        pass


class Link(FileSystemOp):
    def __init__(self, src, dst, **kwargs):
        pass

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class Remove(FileSystemOp):
    def __init__(self, target, **kwargs):
        pass

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class RemoveDir(FileSystemOp):
    def __init__(self, target, **kwargs):
        pass

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class Copy(FileSystemOp):
    def __init__(self, src, dst, **kwargs):
        pass

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class Move(FileSystemOp):
    def __init__(self, src, dst, **kwargs):
        pass

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class FsOpQueue(FileSystemOp):
    def __init__(self, *ops, **kwargs):
        self.ops = ops

    def validate(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


def main():
    pass
    # .bashrc
    # cp -L ~/.bashrc .
    # rm ~/.bashrc
    # ln -s dotfiles/.bashrc ~/.bashrc

    # OpenSSH Server
    # sudo apt update
    # sudo apt install openssh-server
    # sudo systemctl status ssh
    # sudo ufw allow ssh


if __name__ == "__main__":
    main()
