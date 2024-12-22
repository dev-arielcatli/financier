import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { COMMA, ENTER } from '@angular/cdk/keycodes';

import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogRef,
} from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import {
  MatChipEditedEvent,
  MatChipInputEvent,
  MatChipsModule,
} from '@angular/material/chips';
import { CommonModule } from '@angular/common';
import { SafeDisplayIncome } from '../income.model';

@Component({
  selector: 'fn-income-form',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogActions,
    MatButtonModule,
    MatIconModule,
    MatChipsModule,
    CommonModule,
  ],
  templateUrl: './income-form.component.html',
  styleUrl: './income-form.component.scss',
})
export class IncomeFormComponent {
  private formBuilder = inject(FormBuilder);

  incomeDialogRef = inject(MatDialogRef<IncomeFormComponent>);

  dialogData: SafeDisplayIncome = inject(MAT_DIALOG_DATA);

  incomeForm = this.formBuilder.group({
    id: [''],
    name: ['', Validators.required],
    description: [''],
    quantity: [1, Validators.required],
    amount: [0, Validators.required],
    date: [''],
    createdAt: [''],
    updatedAt: [''],
    address: [''],
    sources: [[]],
    tags: [[]],
  });

  // CHIPS
  readonly separatorKeysCodes = [ENTER, COMMA] as const;

  constructor() {
    if (this.dialogData) {
      this.incomeForm.patchValue(this.dialogData);
    }
  }

  get tags(): string[] {
    return this.incomeForm.value.tags || [];
  }

  get sources(): string[] {
    return this.incomeForm.value.sources || [];
  }

  onSave(): void {
    if (this.incomeForm.valid) {
      this.incomeDialogRef.close(this.incomeForm.value);
    }
  }

  onCancel(): void {
    this.incomeDialogRef.close();
  }

  addTag(event: MatChipInputEvent): void {
    const newTag = (event.value || '').trim();
    if (newTag) {
      this.incomeForm.controls.tags.patchValue(
        // TODO: Fix issue with this model
        this.tags.concat(newTag) as any,
      );
    }
    event.chipInput!.clear();
  }

  addSource(event: MatChipInputEvent): void {
    const newSource = (event.value || '').trim();
    if (newSource) {
      this.incomeForm.controls.sources.patchValue(
        // TODO: Fix issue with this model
        this.sources.concat(newSource) as any,
      );
    }
    event.chipInput!.clear();
  }

  removeTag(tag: string): void {
    this.incomeForm.controls.tags.patchValue(
      // TODO: Fix issue with this model
      this.tags.filter((t) => t !== tag) as any,
    );
  }

  removeSources(source: string): void {
    this.incomeForm.controls.sources.patchValue(
      // TODO: Fix issue with the model
      this.sources.filter((s) => s !== source) as any,
    );
  }
}
