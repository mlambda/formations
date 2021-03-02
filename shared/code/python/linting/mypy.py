class TargetBuilder:
    def _parse_section_dir(
        self, section_path: str, custom_config: Dict[str, Any],
    ) -> Optional[Tuple[Section, Dependencies]]:
        ...
