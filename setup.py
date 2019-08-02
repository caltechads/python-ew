import os

from distutils.core import setup, Extension

EW_HOME = os.getenv('EW_HOME')
libs = EW_HOME + '/lib/'
includes = EW_HOME + '/include/'

tracebuf2_module = Extension(
    name='python_ew.tracebuf2.tracebuf2module',
    sources=['python_ew/tracebuf2/tracebuf2module.c'],
    include_dirs=[includes],
    library_dirs=[libs],
    extra_objects=[
        '%sringwriter.o' % libs,
        '%sringreader.o' % libs,
        '%stransport.o' % libs,
        '%sgetutil.o' % libs,
        '%skom.o' % libs,
        '%ssleep_ew.o' % libs,
        '%slogit.o' % libs,
        '%stime_ew.o' % libs,
        '%sswap.o' % libs
    ],
    extra_compile_args=[
        '-fPIC',
        '-m64',
        '-Dlinux',
        '-D_LINUX',
        '-D_INTEL',
        '-D_USE_SCHED',
        '-D_USE_PTHREADS',
        '-D_USE_TERMIOS'
    ],
    extra_link_args=[
        '-lm',
        '-lpthread'
    ]
)


status_module = Extension(
    name='python_ew.status.statusmodule',
    sources=['python_ew/status/statusmodule.c'],
    include_dirs=[includes],
    library_dirs=[libs],
    extra_objects=[
        '%sringwriter.o' % libs,
        '%sringreader.o' % libs,
        '%stransport.o' % libs,
        '%sgetutil.o' % libs,
        '%skom.o' % libs,
        '%ssleep_ew.o' % libs,
        '%slogit.o' % libs,
        '%stime_ew.o' % libs,
        '%sswap.o' % libs
    ],
    extra_compile_args=[
        '-fPIC',
        '-m64',
        '-Dlinux',
        '-D_LINUX',
        '-D_INTEL',
        '-D_USE_SCHED',
        '-D_USE_PTHREADS',
        '-D_USE_TERMIOS'
    ],
    extra_link_args=[
        '-lm',
        '-lpthread'
    ]
)


heartbeat_module = Extension(
    name='python_ew.heartbeat.heartbeatmodule',
    sources=['python_ew/heartbeat/heartbeatmodule.c'],
    include_dirs=[includes],
    library_dirs=[libs],
    extra_objects=[
        '%sringwriter.o' % libs,
        '%sringreader.o' % libs,
        '%stransport.o' % libs,
        '%sgetutil.o' % libs,
        '%skom.o' % libs,
        '%ssleep_ew.o' % libs,
        '%slogit.o' % libs,
        '%stime_ew.o' % libs,
        '%sswap.o' % libs
    ],
    extra_compile_args=[
        '-fPIC',
        '-m64',
        '-Dlinux',
        '-D_LINUX',
        '-D_INTEL',
        '-D_USE_SCHED',
        '-D_USE_PTHREADS',
        '-D_USE_TERMIOS'
    ],
    extra_link_args=[
        '-lm',
        '-lpthread'
    ]
)


setup(
    name='python_ew',
    version='1.0.0',
    description='Modules that can interact with Earthworm Rings.',
    packages=['python_ew', 'python_ew.heartbeat', 'python_ew.status', 'python_ew.tracebuf2'],
    ext_modules=[
        tracebuf2_module,
        status_module,
        heartbeat_module
    ]
)
