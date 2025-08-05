#!/usr/bin/env python3
"""
PyCompiler CLI
Simple and direct Python to Native Executable Builder.
"""

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from src.builder import Builder, Config


class CompilerCLI:
    def __init__(self):
        self._console = Console()

    def print_banner(self):
        """Display elegant banner."""
        banner_text = Text()
        banner_text.append("PyCompiler", style="bold blue")
        banner_text.append(" - Python to Native Builder", style="dim")

        panel = Panel(banner_text, border_style="blue", padding=(0, 1))
        self._console.print(panel)

    def print_help(self):
        """Display custom help."""
        self.print_banner()

        help_text = Text()
        help_text.append("Usage:\n", style="bold")
        help_text.append("  python compiler.py          # Build project\n", style="white")
        help_text.append("  python compiler.py --info    # Show project info\n", style="white")
        help_text.append("  python compiler.py --config my.yaml\n", style="white")
        help_text.append("  python compiler.py --show-help  # Show this help\n\n", style="white")
        help_text.append("Examples:\n", style="bold")
        help_text.append("  python compiler.py\n", style="dim")
        help_text.append("  python compiler.py --info\n", style="dim")
        help_text.append("  python compiler.py --config my_config.yaml", style="dim")

        panel = Panel(help_text, title="Help", border_style="green")
        self._console.print(panel)

    def build_project(self, config_path: str):
        """Build the project."""
        try:
            # Load configuration
            config = Config(config_path)

            # Project info panel
            info_text = Text()
            info_text.append("Project: ", style="bold")
            info_text.append(f"{config.project_name}\n", style="cyan")
            info_text.append("Main: ", style="bold")
            info_text.append(f"{config.main_file} → {config.output_name}", style="cyan")

            info_panel = Panel(info_text, title="Build Info", border_style="blue")
            self._console.print(info_panel)

            # Create builder
            builder = Builder(config)

            # Build with elegant progress
            with Progress(
                SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=self._console
            ) as progress:
                # Environment creation
                task1 = progress.add_task("Creating environment...", total=1)
                builder.create_temp_env()
                progress.update(task1, completed=1, description="✓ Environment created")

                # Dependencies installation
                task2 = progress.add_task("Installing dependencies...", total=1)
                builder.install_dependencies()
                progress.update(task2, completed=1, description="✓ Dependencies installed")

                # Compilation
                task3 = progress.add_task("Compiling with Nuitka...", total=1)
                builder.build_with_nuitka()
                progress.update(task3, completed=1, description="✓ Compilation completed")

                # Cleanup
                task4 = progress.add_task("Cleaning up...", total=1)
                builder.cleanup()
                progress.update(task4, completed=1, description="✓ Cleanup finished")

            # Success panel
            success_text = Text()
            success_text.append("Build completed successfully!", style="bold green")
            success_text.append(f"\nOutput: {config.output_name}", style="cyan")

            success_panel = Panel(success_text, title="Success", border_style="green")
            self._console.print(success_panel)

        except KeyboardInterrupt:
            self._console.print("\n[yellow]⚠ Build interrupted[/yellow]")
            sys.exit(1)

        except Exception as exception:
            error_text = Text()
            error_text.append("Build failed!", style="bold red")
            error_text.append(f"\nError: {exception}", style="red")

            error_panel = Panel(error_text, title="Error", border_style="red")
            self._console.print(error_panel)
            sys.exit(1)

    def show_info(self, config_path: str):
        """Show project information."""
        try:
            config = Config(config_path)

            table = Table(title="Project Information", show_header=True, header_style="bold magenta")
            table.add_column("Property", style="cyan", no_wrap=True)
            table.add_column("Value", style="white")

            table.add_row("Project Name", config.project_name)
            table.add_row("Main File", config.main_file)
            table.add_row("Output Name", config.output_name)

            if config.icon_file:
                table.add_row("Icon File", config.icon_file)
            else:
                table.add_row("Icon File", "[dim]None[/dim]")

            # Show dependencies count
            deps_count = len(config.project_libs) if config.project_libs else 0
            deps_text = f"{deps_count} libraries" if deps_count > 0 else "None"
            table.add_row("Dependencies", deps_text)

            # Show packages count
            packages_count = len(config.include_packages) if config.include_packages else 0
            packages_text = f"{packages_count} packages" if packages_count > 0 else "None"
            table.add_row("Include Packages", packages_text)

            self._console.print(table)

        except Exception as e:
            error_text = Text()
            error_text.append("Failed to load project info!", style="bold red")
            error_text.append(f"\nError: {e}", style="red")

            error_panel = Panel(error_text, title="Error", border_style="red")
            self._console.print(error_panel)

    def run(self):
        """Main CLI entry point."""
        parser = argparse.ArgumentParser(description="PyCompiler")
        parser.add_argument("--config", "-c", default="config.yaml", help="Config file (default: config.yaml)")
        parser.add_argument("--info", action="store_true", help="Show project info")
        parser.add_argument("--show-help", action="store_true", help="Show detailed help")

        args = parser.parse_args()

        # Handle custom help
        if args.show_help:
            self.print_help()
            return

        # Show banner
        self.print_banner()

        # Check if config exists
        if not Path(args.config).exists():
            error_text = Text()
            error_text.append(f"Config file not found: {args.config}", style="red")
            error_text.append("\nCreate config.yaml with your project settings", style="dim")

            error_panel = Panel(error_text, title="Error", border_style="red")
            self._console.print(error_panel)
            sys.exit(1)

        # Execute
        if args.info:
            self.show_info(args.config)
        else:
            self.build_project(args.config)


def main():
    """Entry point."""
    cli = CompilerCLI()
    cli.run()


if __name__ == "__main__":
    main()
