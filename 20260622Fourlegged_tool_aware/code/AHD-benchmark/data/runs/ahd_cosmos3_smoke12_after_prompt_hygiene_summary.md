# Cosmos3 Run Summary: ahd_cosmos3_smoke12_after_prompt_hygiene_results

- total: 12
- success: 7
- failed: 5
- success_rate: 58.3%

## Width/Height Distribution

- 960x960: 7

## Counts By Spec Type

- aggregate_transport_o0_target_visible_helper_absent: 0/2 success
- container_helper_o1_target_absent: 0/2 success
- direct_is_enough_o0_single_target: 1/2 success
- extend_reach_o0_target_under_furniture: 2/2 success
- long_tool_helper_o1_target_absent: 2/2 success
- wrong_helper_o1_target_absent: 2/2 success

## Failures

- agg_o0_000001:         config, *args, recursive=_recursive_, convert=_convert_, partial=_partial_
    )
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 452, in instantiate_node
    return _call_target(_target_, partial, args, kwargs, full_key)
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 187, in _call_target
    raise InstantiationException(msg) from e
hydra.errors.InstantiationException: Error in call to target 'cosmos_framework.model.generator.omni_mot_model.OmniMoTModel':
OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated by PyTorch, and 23.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)')
output_dir files: ['console.log (8439 bytes)', 'debug.log (14155 bytes)']
- agg_o0_000002:         config, *args, recursive=_recursive_, convert=_convert_, partial=_partial_
    )
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 452, in instantiate_node
    return _call_target(_target_, partial, args, kwargs, full_key)
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 187, in _call_target
    raise InstantiationException(msg) from e
hydra.errors.InstantiationException: Error in call to target 'cosmos_framework.model.generator.omni_mot_model.OmniMoTModel':
OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated by PyTorch, and 23.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)')
output_dir files: ['console.log (8439 bytes)', 'debug.log (14155 bytes)']
- container_o1_000001:         config, *args, recursive=_recursive_, convert=_convert_, partial=_partial_
    )
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 452, in instantiate_node
    return _call_target(_target_, partial, args, kwargs, full_key)
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 187, in _call_target
    raise InstantiationException(msg) from e
hydra.errors.InstantiationException: Error in call to target 'cosmos_framework.model.generator.omni_mot_model.OmniMoTModel':
OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated by PyTorch, and 23.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)')
output_dir files: ['console.log (8439 bytes)', 'debug.log (14167 bytes)']
- container_o1_000002:         config, *args, recursive=_recursive_, convert=_convert_, partial=_partial_
    )
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 452, in instantiate_node
    return _call_target(_target_, partial, args, kwargs, full_key)
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 187, in _call_target
    raise InstantiationException(msg) from e
hydra.errors.InstantiationException: Error in call to target 'cosmos_framework.model.generator.omni_mot_model.OmniMoTModel':
OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated by PyTorch, and 23.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)')
output_dir files: ['console.log (8438 bytes)', 'debug.log (14166 bytes)']
- direct_o0_000001:         config, *args, recursive=_recursive_, convert=_convert_, partial=_partial_
    )
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 452, in instantiate_node
    return _call_target(_target_, partial, args, kwargs, full_key)
  File "/data0/yurunze/conda_envs/codex_cosmos/lib/python3.13/site-packages/hydra/_internal/instantiate/_instantiate2.py", line 187, in _call_target
    raise InstantiationException(msg) from e
hydra.errors.InstantiationException: Error in call to target 'cosmos_framework.model.generator.omni_mot_model.OmniMoTModel':
OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated by PyTorch, and 23.31 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)')
output_dir files: ['console.log (8439 bytes)', 'debug.log (14161 bytes)']
