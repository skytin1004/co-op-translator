from __future__ import annotations

import asyncio
import logging

from tqdm import tqdm

logger = logging.getLogger(__name__)


class TranslationTaskExecutorMixin:
    async def process_api_requests_parallel(self, tasks, task_desc) -> list:
        """Execute multiple API requests concurrently with controlled parallelism.

        Uses a queue system to manage API requests efficiently while providing
        progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        async def run_task(task):
            try:
                if asyncio.iscoroutine(task):
                    return await task
                if asyncio.iscoroutinefunction(task):
                    return await task()
                if callable(task):
                    result = await asyncio.to_thread(task)
                    if asyncio.iscoroutine(result):
                        return await result
                    return result
                return task
            except Exception as e:
                logger.error(f"Error processing task: {e}")
                return None

        semaphore = asyncio.Semaphore(5)

        async def run_limited(task, progress_bar):
            async with semaphore:
                try:
                    return await run_task(task)
                finally:
                    progress_bar.update(1)

        with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
            return await asyncio.gather(
                *(run_limited(task, progress_bar) for task in tasks)
            )

    async def process_api_requests_sequential(
        self, tasks, task_desc, file_names=None
    ) -> list:
        """Execute API requests one at a time in sequence.

        Ensures requests are processed in order while providing progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        total_tasks = len(tasks)

        results = []
        with tqdm(total=total_tasks, desc=task_desc) as progress_bar:
            for i, task in enumerate(tasks):
                # Show current file name in progress bar if available
                if file_names and i < len(file_names):
                    file_name = file_names[i]
                    progress_bar.set_description(f"🔄 Translating: {file_name}")

                # Execute task and get result
                result = await task()  # Execute each task sequentially
                results.append(result)

                # Update progress bar
                progress_bar.update(1)

                # Reset description after completion if needed
                if i + 1 < total_tasks:
                    progress_bar.set_description(task_desc)

        return results
