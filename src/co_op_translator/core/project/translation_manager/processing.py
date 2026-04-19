"""Task-processing helpers for translation workflows."""

from __future__ import annotations

import asyncio
import logging

from tqdm import tqdm

from co_op_translator.utils.common.task_utils import worker

logger = logging.getLogger(__name__)


async def process_api_requests_parallel(tasks, task_desc) -> list:
    """Execute multiple API requests concurrently with controlled parallelism."""
    if not tasks:
        logger.warning("No tasks available for processing.")
        return []

    task_queue = asyncio.Queue()
    for task in tasks:
        task_queue.put_nowait(task)

    worker_count = 5
    for _ in range(worker_count):
        task_queue.put_nowait(None)

    with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
        workers = [
            asyncio.create_task(worker(task_queue, progress_bar))
            for _ in range(worker_count)
        ]

        await task_queue.join()
        results = [task.result() for task in workers]

    return results


async def process_api_requests_sequential(tasks, task_desc, file_names=None) -> list:
    """Execute API requests one at a time in sequence."""
    if not tasks:
        logger.warning("No tasks available for processing.")
        return []

    results = []
    with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
        for index, task in enumerate(tasks):
            if file_names and index < len(file_names):
                progress_bar.set_description(f"🔄 Translating: {file_names[index]}")

            result = await task()
            results.append(result)
            progress_bar.update(1)

            if index + 1 < len(tasks):
                progress_bar.set_description(task_desc)

    return results
